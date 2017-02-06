from django.contrib.auth.models import User
from rest_framework import serializers

from collectors.user.models import Friendship


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User
    """

    class Meta:
        model = User
        fields = (
            'id',
        )


class FriendshipSerializer(serializers.ModelSerializer):
    creator = UserSerializer
    friend = UserSerializer

    class Meta:
        model = Friendship
        fields = (
            'id',
            'creator',
            'friend',
        )
