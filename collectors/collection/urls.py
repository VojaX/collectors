from django.conf.urls import url, include
from rest_framework import routers
from collectors.collection.views import CollectionListAPIView
from . import views


api_urls = [
    url(
        r'^$',
        views.CollectionListAPIView.as_view(),
        name='list'
    ),
]
