from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your basket at present!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JH3yzBD8gNnPvi4Oe4lANthMin0ffy4HjejEiy6IXkmzkDsSxtQNMGaEdtD2LA4gLMOJHxDZR3dsJl5S4d5xaqo00QhE5E9k0',
        'client_secret': 'secret'
    }

    return render(request, template, context)
