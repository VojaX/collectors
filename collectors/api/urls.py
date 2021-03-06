from django.conf.urls import url, include
from rest_framework import routers

from collectors.collection.views import CollectionListAPIView

router = routers.DefaultRouter()
router.register(r'collection', CollectionListAPIView)
urlpatterns = [

    url(r'^', include(router.urls)),
]
