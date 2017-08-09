from django.urls import resolve, reverse
from django.test import TestCase
from django.http import HttpRequest

#from wiki.views import home_page

# Create your tests here.
class QueryPageTest(TestCase):

    def test_uses_query_template(self):
        response = self.client.get('/query/')

        self.assertTemplateUsed(response, 'wiki/query.html')