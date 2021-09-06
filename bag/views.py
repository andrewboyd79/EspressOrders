from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/basket.html')


def add_to_bag(request, item_id):
    """ Adds number of a product to the bag """

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
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        item_size = None
        if 'item_size' in request.POST:
            item_size = request.POST['item_size']
        bag = request.session.get('bag', {})

        if item_size:
            del bag[item_id]['items_by_size'][item_size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
