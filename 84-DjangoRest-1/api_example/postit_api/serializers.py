from rest_framework import serializers
from .models import Post, Comment, CommentLike, PostLike

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    
    class Meta:
        model = Post
        fields = ['id', 'user', 'user_id', 'title', 'body', 'created']