from django.shortcuts import render
from .models import Location


def index(request):
    """
    A view created to return the index/home page along with locations
    """
    location = Location.objects.all()

    context = {
        'location': location,
    }

    return render(request, 'home/index.html', context)
