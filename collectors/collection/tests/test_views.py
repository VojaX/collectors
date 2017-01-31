from cities_light.models import Country, City
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from collectors.collection.factories import CollectionFactory


class CollectionListAPIViewTests(APITestCase):
    fixtures = [
        'fixtures/test_countries',
        'fixtures/test_regions',
        'fixtures/test_cities',
    ]

    def test_list(self):
        CollectionFactory.create_batch(3)
        url = reverse('api.collection:list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)


class CollectionDetailAPIViewTests(APITestCase):
    fixtures = [
        'fixtures/test_countries',
        'fixtures/test_regions',
        'fixtures/test_cities',
    ]

    def test_detail(self):
        collection = CollectionFactory()
        url = reverse('api.collection:detail', kwargs={
            'pk': collection.pk
        })

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], collection.id)
