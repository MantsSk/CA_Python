from django.urls import path, include
from .views import PostList, PostDetail, CommentList, PostComments, CommentDetail, PostLikeCreate

urlpatterns = [
    path('posts', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('comments', CommentList.as_view()),
    path('comments/<int:pk>', CommentDetail.as_view()),
    path('posts/<int:pk>/comments/', PostComments.as_view()),
    path('posts/<int:pk>/comments/', PostComments.as_view()),
    path('posts/<int:pk>/like', PostLikeCreate.as_view()),
]
