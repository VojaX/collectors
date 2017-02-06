from rest_framework import generics

from collectors.comments.models import Comment
from collectors.comments.serializers import CommentSerializer


class CommentListAPIView(generics.ListAPIView):
    """
    Collection list endpoint
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailAPIView(generics.RetrieveAPIView):
    """
    Collection detail endpoint
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
