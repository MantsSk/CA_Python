from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:author_id>', views.author, name='author'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('search/', views.search, name='search'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
