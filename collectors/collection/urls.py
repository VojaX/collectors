from django.conf.urls import url
from . import views


api_urls = [
    url(
        r'^$',
        views.CollectionListAPIView.as_view(),
        name='list'
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        views.CollectionDetailAPIView.as_view(),
        name='detail'
    ), 
]
