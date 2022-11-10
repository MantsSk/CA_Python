from django.urls import path, include
from .views import PostList, PostDetail, CommentList, PostsCommentList

urlpatterns = [
    path('posts', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('comments', CommentList.as_view()),
    path('posts/<int:pk>/comments', PostsCommentList.as_view()),
]
