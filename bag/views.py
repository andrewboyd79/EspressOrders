from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """
    A view that renders the bag contents page
    """

    return render(request, 'bag/basket.html')


def add_to_bag(request, item_id):
    """
    Adds number of a product to the bag
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    item_size = None

    if 'product_size' in request.POST:
        item_size = request.POST['product_size']

    bag = request.session.get('bag', {})

    if item_size:
        if item_id in list(bag.keys()):
            if item_size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][item_size] += quantity
            else:
                bag[item_id]['items_by_size'][item_size] = quantity
        else:
            bag[item_id] = {'items_by_size': {item_size: quantity}}

        messages.success(request, f'Thanks! A {product.name} has been added \
                            to your basket')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

        messages.success(request, f'Thanks! A {product.name} has been added \
                            to your basket')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """
    Remove the item from the shopping bag
    """

    try:
        product = get_object_or_404(Product, pk=item_id)
        item_size = None
        if 'item_size' in request.POST:
            item_size = request.POST['item_size']
        bag = request.session.get('bag', {})

        if item_size:
            del bag[item_id]['items_by_size'][item_size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'{product.name} removed\
                             from your basket')
        else:
            bag.pop(item_id)
            messages.success(request, f'{product.name} removed\
                             from your basket')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
