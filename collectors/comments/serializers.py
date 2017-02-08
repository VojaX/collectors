from rest_framework import serializers

from collectors.collection.serializers import CollectionListSerializer, \
    CollectionSerializer
from collectors.user.serializers import UserSerializer
from . import models


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for CollectionType
    """
    collection = CollectionSerializer
    owner = UserSerializer

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'body',
            'collection',
            'owner',
        )
