from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    basket_items = []
    basket_total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            starting_price = product.starting_price
            item_total = item_data * product.starting_price
            basket_total += item_total
            product_count += item_data

            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'starting_price': starting_price,
                'item_total': item_total,

            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for item_size, quantity in item_data['items_by_size'].items():
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
                    'item_size': item_size,
                })

    context = {
        'basket_items': basket_items,
        'basket_total': basket_total,
        'product_count': product_count,

    }

    return context
