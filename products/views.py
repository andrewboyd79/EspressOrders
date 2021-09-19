from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Type
from .forms import ProductForm


def all_products(request):
    """
    A view created to show all the products
    """

    products = Product.objects.all()
    categories = None
    types = None
    query = None
    location = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            types = Type.objects.filter(category__in=categories)

        if 'type' in request.GET:
            types = request.GET['type'].split(',')
            products = products.filter(type__name__in=types)
            types = Type.objects.filter(name__in=types)

        if 'location' in request.GET:
            location = request.GET['location']
            types = Type.objects.all()
            request.session['selected_location'] = location

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "OOPS!! You didn't enter anything!! \
                                 Please try again")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)

            products = products.filter(queries)
            types = Type.objects.all()

    else:
        types = Type.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'types': types,
        'search': query,
        'location': location,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view created to show all the detail of the selcted product
    """

    product = get_object_or_404(Product, pk=product_id)
    ordering_location = request.session['selected_location']

    context = {
        'product': product,
        'ordering_location': ordering_location,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
