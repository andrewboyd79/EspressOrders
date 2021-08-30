from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Type

# Create your views here.


def all_products(request):
    """
    A view created to show all the products
    """

    products = Product.objects.all()
    categories = Category.objects.all()
    types = Type.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'types': types,
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
