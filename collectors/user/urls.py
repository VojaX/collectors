from django.conf.urls import url
from . import views


api_urls = [
    url(
        r'^friendship/(?P<pk>[0-9]+)/$',
        views.FriendshipDetailAPIView.as_view(),
        name='detail'
    ),
    url(
        r'^friendship/create/$',
        views.FriendshipCreateAPIView.as_view(), name='create'),
]
