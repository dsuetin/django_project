from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe
from basket.basket import Basket


@login_required
def BasketView(request):
    """class for rendering basket"""
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)
    print('total', total)
    stripe.api_key = 'sk_test_51OqvirER9Ror46DFVe6mSQgvDpJdansMmgKMp3nGzUxroWpR4ZHfnnfSCkASyhJ4lZE2eQMjOvgSlYhkk6VkTbj300jSCkspk9'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )
    
    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})

