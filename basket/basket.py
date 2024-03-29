"""

"""

from decimal import Decimal

from django.conf import settings

from store.models import Product


class Basket():
    """
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if settings.BASKET_SESSION_ID not in self.session:
            basket = self.session[settings.BASKET_SESSION_ID] = {}  # {'number': 91919183}
        self.basket = basket

    def add(self, product, qty=1):
        """
        Add product to basket
        """
        product_id = str(product.id)
        print('add product_id', product_id, self.basket, str(product_id) in self.basket)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty':
                                       qty}
        # self.save()
        self.session[settings.BASKET_SESSION_ID] = self.basket
        self.save()
        # self.session.modified = True
        # from django.contrib.sessions.models import Session
        # s = Session.objects.get(pk='fbsljzqwkgm6bk1tkciflde5c18lkn44')

    def __iter__(self):
        """
        """
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product3'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        """
        Get the basket data and count qty
        """
        return sum(item['qty'] for item in self.basket.values())

    def get_total_price(self):
        """
        Calculate the total price of the basket
        """
        subtotal = sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

        if subtotal == 0:
            shipping = Decimal(0)
        else:
            shipping = Decimal(11.5)
        total = subtotal + shipping
        return total

    def delete(self, product):
        """
        """
        product_id = str(product)
        print('product_id', type(product_id), product_id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def update(self, product, qty):
        """
        Updates the quantity of a product in the basket in session
        """
        product_id = str(product)
        qty = qty

        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        self.save()

    def save(self):
        """
        Save session changes
        """
        self.session.modified = True

    def clear(self):
        """ Remove all items from the basket """
        del self.session[settings.BASKET_SESSION_ID]
        self.save()
