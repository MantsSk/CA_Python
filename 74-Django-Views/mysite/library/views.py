from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
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