from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.
from store.models import Category, Product
from unittest import skip

from django.test import Client

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
        self.data1 = Product(category_id=1, title='django beginers', created_by_id=1, slug='slug django', price='20.00', image='imgae_django')
        
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
    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)