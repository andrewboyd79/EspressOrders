from django.shortcuts import render
from .models import Location, Cart


def index(request):
    """
    A view created to return the index/home page along with locations
    """
    location = Location.objects.all()

    context = {
        'location': location,
    }

    return render(request, 'home/index.html', context)


def about_us(request):
    """
    A view created to return the about us page along with the cart info
    """
    cart = Cart.objects.all()

    context = {
        'cart': cart,
    }

    return render(request, 'home/about_us.html', context)
