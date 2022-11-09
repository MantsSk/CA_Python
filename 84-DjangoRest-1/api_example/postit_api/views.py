from django.shortcuts import render
from rest_framework import generics, permissions # papildomai importuojame permissions!
from .models import Post, PostLike, Comment, CommentLike
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)