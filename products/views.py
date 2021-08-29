from django.shortcuts import render
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
