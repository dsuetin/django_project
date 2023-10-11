"""_summary_ """
from django.shortcuts import render

from .models import Category, Product

def all_poducts(request):
    """get all products

    Args:
        request (_type_): _description_
    """
    pass
    # products = Product.objects.all()
    products = ['ddd', 'wwww']
    return render(request, 'store/home.html', {'products': products})
