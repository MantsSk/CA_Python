from django.urls import path, include
from .views import PostList

urlpatterns = [
    path('postukai', PostList.as_view()),
]