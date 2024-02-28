from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Product, Category


class TestBasketView(TestCase):
    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                               slug='django', price=20, image='django')
        Product.objects.create(category_id=1, title='django intemediate', created_by_id=1,
                               slug='django', price=20, image='django')
        Product.objects.create(category_id=1, title='django advanced', created_by_id=1,
                               slug='django', price=20, image='django')
        self.client.post(
            reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xht=True
        )
        self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 2, "action": "post"}, xht=True
        )
       
    def test_basket_url(self):
        """
        """
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        """
        """
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 3, "productqty": 1, "action": "post"}, xht=True)
        # print("response.json", response.json)
        # for j, v in response.json().items():
        #     print("2222222222222222222222222", j, v)
        self.assertEqual(response.json(), {'qty': 4})
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 1, "action": "post"}, xht=True)
        self.assertEqual(response.json(), {'qty': 3})

    def test_basket_delete(self):
        """
        test for delete product from basket
        """
        response = self.client.post(
            reverse('basket:basket_delete'), {"productid": 2, "action": "post"}, xht=True)
        self.assertEqual(response.json(), {'qty': 1, 'subtotal': '20.00'})
        
    def test_basket_update(self):
        """
        test for update product quantity in basket
        """
        response = self.client.post(
            reverse('basket:basket_update'), {"productid": 2, "productqty": 1, "action": "post"}, xht=True)
        self.assertEqual(response.json(), {'qty': 2, 'subtotal': '40.00'})
