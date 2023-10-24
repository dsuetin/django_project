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


def products_all(request):
    """get all products

    Args:
        request (_type_): _description_
    """
    # products = Product.objects.all()
    products = Product.objects.filter(is_active=True)
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    print("category_slug", category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})
