from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from collectors.user.models import Friendship
from collectors.user.serializers import FriendshipSerializer


class FriendshipDetailAPIView(generics.RetrieveAPIView):
    """
    Collection detail endpoint
    """
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer


class FriendshipCreateAPIView(generics.CreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = FriendshipSerializer
    queryset = Friendship.objects.all().exclude()