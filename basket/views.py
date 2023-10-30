from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from store.models import Product

from .basket import Basket


def basket_summary(request):
    # basket = Basket(request)
    # return render(request, 'store/basket/summary.html', {'basket': basket})
    print("request, basket_summary", request)
    return render(request, 'store/basket/summary.html')

# s = Session.objects.get(pk='wyx1l8hrcsg9a7bugtn8960g40guf72c')


def basket_add(request):
    # print('basket_add', request)
    print('basket_add')
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        print('product_id', product_id)
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product)
        response = JsonResponse({'test': 'data'})
        print('basket_add response', response)
        # response = {}
        return response
