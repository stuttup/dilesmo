from django.urls import resolve
from django.test import TestCase
from .views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func.__dict__, home_page.__dict__)