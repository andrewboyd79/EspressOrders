from django.shortcuts import render

# Create your views here.


def index(request):
    """
    A view created to return the index/home page
    """

    return render(request, 'home/index.html')
