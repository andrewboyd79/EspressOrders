from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    basket_items = []
    basket_total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        starting_price = product.starting_price
        item_total = quantity * product.starting_price
        basket_total += item_total
        product_count += quantity

        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'starting_price': starting_price,
            'item_total': item_total,

        })

    context = {
        'basket_items': basket_items,
        'basket_total': basket_total,
        'product_count': product_count,

    }

    return context
