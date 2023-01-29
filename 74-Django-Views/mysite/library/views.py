from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):

    # Suskaičiuokime keletą pagrindinių objektų
    book_count = Book.objects.all().count()
    book_instance_count = BookInstance.objects.all().count()

    # Laisvos knygos (tos, kurios turi statusą 'av')
    available_book_instances_available = BookInstance.objects.filter(
        status='av').count()

    # Autorių skaičius
    author_count = Author.objects.all().count()

    context = {
        'book_count': book_count,
        'book_instance_count': book_instance_count,
        'available_book_instances_available': available_book_instances_available,
        'author_count': author_count
    }

    return render(request, 'index.html', context=context)


def authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }

    return render(request, 'authors.html', context=context)


def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {
        'author': author
    }
    return render(request, 'author.html', context=context)


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'book_list'
    template_name = 'book_list.html'
    queryset = Book.objects.filter(title='Title 1')

    def get_queryset(self):
        return Book.objects.filter(title='Title 1')

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['duomenys'] = 'Random text'
        return context


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'
