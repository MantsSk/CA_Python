from django.urls import path

from .views import PostList, PostDetail, CommentList, PostComments, CommentDetail, UserCreate

urlpatterns = [
    path('posts', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('comments', CommentList.as_view()),
    path('comments/<int:pk>', CommentDetail.as_view()),
    path('posts/<int:pk>/comments/', PostComments.as_view()),
    path('posts/<int:pk>/comments/', PostComments.as_view()),
    path('signup', UserCreate.as_view()),
]
