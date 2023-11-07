
class Basket():
    """
    """
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in self.session:
            basket = self.session['skey'] = {}  # {'number': 91919183}
        self.basket = basket

    def add(self, product, qty=1):
        """
        """
        product_id = str(product.id)
        print('add product_id', product_id, self.basket, str(product_id) in self.basket)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': 
                                       qty}
        # self.save()
        self.session['skey'] = self.basket

        self.session.modified = True
        # from django.contrib.sessions.models import Session
        # s = Session.objects.get(pk='fbsljzqwkgm6bk1tkciflde5c18lkn44')

    def __len__(self):
        """
        Get the basket data and count qty
        """
        return sum(item['qty'] for item in self.basket.values())
