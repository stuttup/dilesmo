from django.urls import resolve, reverse
from django.test import TestCase
from django.http import HttpRequest

from wiki.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func.__dict__, home_page().__dict__)

    def test_home_page_returns_correct_html(self):
        # request = HttpRequest()
        # found = resolve('/')
        # response = found.__class__()(request)
        # html = response.content.decode('uft8')
        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>Dilesmo</title>', html)
        # self.assertTrue(html.endswith('</html>'))
        pass
