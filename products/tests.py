from django.test import TestCase
from .models import Product

class ProductTests(TestCase):
    """
    Defining tests (methods starting with 'test_') that will be run 
    against Product model
    """
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')