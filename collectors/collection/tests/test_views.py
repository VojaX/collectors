from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class CollectionListAPIViewTests(APITestCase):

    def test_list(self):
        CollectionFactory.create_batch(3)
        url = reverse('api.collection:list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)


class CollectionDetailAPIViewTests(APITestCase):
    def test_detail(self):
        collection = CollectionFactory.create_batch()
        url = reverse('api.collection:detail', kwargs={
            'pk': collection.pk
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)
