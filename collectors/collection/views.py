from rest_framework import generics

from collectors.collection.models import Collection
from . import serializers
from . import services

class CollectionListAPIView(generics.ListAPIView):
    """
    Adverts list endpoint
    """
    queryset = Collection.objects.all()
    serializer_class = serializers.CollectionListSerializer

    def get_queryset(self):
        return services.CollectionService.list()

