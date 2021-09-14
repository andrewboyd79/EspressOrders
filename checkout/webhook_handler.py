#  Code taken from CI Boutique Ado walkthrough project

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Order, OrderLineItem
from products.models import Product
from home.models import Location

import json
import time


class StripeWH_Handler:
    """Handles Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle a payment intent succeeded webhook event
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        collection_info = intent.metadata.collection_location
        collection_location = get_object_or_404(Location, pk=collection_info)
        billing_details = intent.charges.data[0].billing_details
        order_total = round(intent.charges.data[0].amount / 100, 2)

        order_exists = False
        attempts = 1
        while attempts <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    collection_location=collection_location,
                    order_total=order_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempts += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                    content=f'Webhook received: {event["type"]} | Success: There is a verified order already in database', status=200)
        else:
            order = None
            print('No orders')
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    collection_location=collection_location,
                    order_total=order_total,
                    original_bag=bag,
                    stripe_pid=pid,
                    )
                print('created')
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for item_size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                item_size=item_size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} | Error code: {e}', status=500
                    )

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | Success: Created order in webhook',
            status=200)

    def handle_payment_intent_failed(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
