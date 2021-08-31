from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Type

# Create your views here.


def all_products(request):
    """
    A view created to show all the products
    """

    products = Product.objects.all()
    categories = None
    types = None
    query = None

    if request.GET:
        if 'type' in request.GET:
            types = request.GET['type'].split(',')
            products = products.filter(type__name__in=types)
            types = Type.objects.filter(name__in=types)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            types = Type.objects.all()

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "OOPS!! You didn't enter anything!! \
                                 Please try again")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)

            products = products.filter(queries)
    else:
        types = Type.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'types': types,
        'search': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view created to show all the detail of the selcted product
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
