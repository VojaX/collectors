from rest_framework import generics

from collectors.collection.models import Collection
from collectors.collection.serializers import CollectionListSerializer


class CollectionListAPIView(generics.ListAPIView):
    """
    Collection list endpoint
    """
    queryset = Collection.objects.all()
    serializer_class = CollectionListSerializer


class CollectionDetailAPIView(generics.RetrieveAPIView):
    """
    Collection detail endpoint
    """
    queryset = Collection.objects.all()
    serializer_class = CollectionListSerializer 
