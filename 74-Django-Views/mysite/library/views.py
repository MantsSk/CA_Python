from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views import generic
from .models import Book, Author, BookInstance, Genre

def index(request):
    
    # Suskaičiuokime keletą pagrindinių objektų
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Laisvos knygos (tos, kurios turi statusą 'g')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # Kiek yra autorių    
    num_authors = Author.objects.count()
    
    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'index.html', context=context)

def authors(request):
    authors = Author.objects.all()

    context = {
        'ne_autoriai': authors
    }

    return render(request, 'authors.html', context)


def author(request, author_id):
    single_author = get_object_or_404(Author, pk=author_id)

    context = {
        'author': single_author
    }
    return render(request, 'author.html', context)

class BookListView(generic.ListView):
    model = Book
    template_name = "book_list.html"

class BookDetailView(generic.DetailView):
    model = Book
    template_name = "book_detail.html"

