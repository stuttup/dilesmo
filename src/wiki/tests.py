#from django.urls import resolve, reverse
from django.test import TestCase
#from django.http import HttpRequest

from wiki.models import Item

# Create your tests here.
class QueryPageTest(TestCase):

    def test_uses_query_template(self):
        response = self.client.get('/query/')

        self.assertTemplateUsed(response, 'wiki/query.html')

    def test_can_save_a_post_request(self):
        self.client.post('/query/', data={'query': 'football'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.title, 'football')


    def test_redirects_after_POST(self):
        response = self.client.post('/query/', data={'query': 'football'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/query/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/query/')
        self.assertEqual(Item.objects.count(), 0)


class ItemmodelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.title = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.title = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.title, 'The first (ever) list item')
        self.assertEqual(second_saved_item.title, 'Item the second')