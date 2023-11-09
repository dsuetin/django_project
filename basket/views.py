from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from store.models import Product

from .basket import Basket


def basket_summary(request):
    # basket = Basket(request)
    # return render(request, 'store/basket/summary.html', {'basket': basket})
    # print("request, basket_summary", request)
    return render(request, 'store/basket/summary.html')

# s = Session.objects.get(pk='wyx1l8hrcsg9a7bugtn8960g40guf72c')


def basket_add(request):
    # print('basket_add', request)
    print('basket_add')
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        print('product_id', product_id)
        print('product_qty', product_qty)
        product = get_object_or_404(Product, id=product_id)
        # basketqty = basket.__len__()
        basket.add(product=product, qty=product_qty)
        # basket.add(product=product, qty=basketqty)
        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        print('basket_add response', response)
        # response = {}
        return response


def basket_delete(request):
    print('basket_delete')
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)
        basketqty = basket.__len__()
        print('basketqty', basketqty)
        baskettotal = basket.get_total_price()
        print('baskettotal', baskettotal)
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket_update(request):
    print('basket_update')
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        print('product_id', product_id)
        print('product_qty', product_qty)
        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
    