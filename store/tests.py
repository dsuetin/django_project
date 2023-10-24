from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import products_all


class TestCategoriesModel(TestCase):
    """Test for model category"""

    def setUp(self):
        self.data1 = Category(name='django', slug='djangorrr')

    def test_category_model_entry(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry_str(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductsModel(TestCase):
    """Test for model products

    Args:
        TestCase (_type_): _description_
    """
    def setUp(self):
        Category(name='django', slug='django')
        User(username='admin')
        self.data1 = Product(category_id=1, title='django beginers', created_by_id=1, slug='django-beginers', price='20.00', image='imgae_django')

    def test_product_model_entry(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))

    def test_product_model_entry_str(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertEqual(str(data), 'django beginers')
        
# @skip("demonstrating skipping")        
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass
    
#     def test_homepage_url(self):
#         """
#         Test homepage response status
#         """
#         response = self.Client.get('/')             


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                               slug='django-beginners', price='20.00', image='django')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='mydonain.com')
        self.assertEqual(response.status_code, 400)
        
    def test_product_detail_url(self):
        """
        Test items response status
        """
        response = self.c.get(
            reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test Category response status
        """
        response = self.c.get(
            reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = products_all(request)
        html = response.content.decode('utf8')
        print(html)
        # self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get('/django-beginners')
        response = products_all(request)
        html = response.content.decode('utf8')
        print(html)
        # self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
