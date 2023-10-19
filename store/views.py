"""_summary_ """
from django.shortcuts import get_object_or_404, render

from .models import Category, Product

def categories(request):
    """ return categories list

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return {
        'categories': Category.objects.all()
    }

def all_poducts(request):
    """get all products

    Args:
        request (_type_): _description_
    """
    pass
    products = Product.objects.all()
    # products = ['ddd', 'wwww']
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug, in_stock=True)
    pass