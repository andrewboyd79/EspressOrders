

def basket_contents(request):

    basket_items = []
    basket_total = 0
    product_count = 0

    context = {
        'basket_items': basket_items,
        'basket_total': basket_total,
        'product_count': product_count,
    }

    return context
