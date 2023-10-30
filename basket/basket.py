
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
        product_id = product.id
        print('add product_id', product_id)
        if product_id not in self.basket:           
            self.basket[product_id] = {'price': float(product.price), 'qty': int(qty)}
            print('add self.basket[product_id]', self.basket[product_id])
        else:
            print('Товар уже добавлен в корзину')
        self.session.modified = True

    # def remove(self, product):