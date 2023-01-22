from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Genre(models.Model):
    name = models.CharField(
        'Title', max_length=200, help_text='Input book\'s genre (for example: detective)')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField('Title', max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        'Summary', max_length=1000, help_text='Short summary of this book')
    isbn = models.CharField(
        'ISBN', max_length=13, help_text='13 symbol <a href="https://www.isbn-international.org/content/what-isbn">ISBN code</a>')
    genre = models.ManyToManyField(Genre, help_text='Genre of this book')

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for a book instance')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(
        'Book will be available at:', null=True, blank=True)

    LOAN_STATUS = (
        ('a', 'Administering'),
        ('t', 'Taken'),
        ('av', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=2,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Status',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField('Last name', max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
