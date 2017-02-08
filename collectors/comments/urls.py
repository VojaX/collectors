from django.conf.urls import url
from . import views


api_urls = [
    url(
        r'^$',
        views.CommentListAPIView.as_view(),
        name='list'
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        views.CommentDetailAPIView.as_view(),
        name='detail'
    ),
    url(
        r'^create/$',
        views.CommentCreateAPIView.as_view(), name='create'),
]
