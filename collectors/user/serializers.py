from django.contrib.auth.models import User
from rest_framework import serializers, fields


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User
    """

    class Meta:
        model = User
        fields = (
            'id',
        )