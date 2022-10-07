import uuid

from django.db import models
from django.urls import reverse  # Papildome imports


class Genre(models.Model):
    name = models.CharField('Pavadinimas', max_length=200,
                            help_text='Įveskite knygos žanrą (pvz. detektyvas)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Žanras'
        verbose_name_plural = 'Žanrai'


class Book(models.Model):
    """Modelis reprezentuoja knygą (bet ne specifinę knygos kopiją)"""
    title = models.CharField(verbose_name="Pavadinimas2", name="title", max_length=200, null=True)
    author = models.ForeignKey(to='author', verbose_name="Autorius", on_delete=models.SET_NULL, null=True, related_name='books')
    summary = models.TextField(verbose_name='Aprašymas', max_length=1000, help_text='Trumpas knygos aprašymas')
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Simbolių <a href="https://www.isbn-international.org/content/what-isbn">ISBN kodas</a>')
    genre = models.ManyToManyField(Genre, help_text='Išrinkite žanrą(us) šiai knygai')

    def __str__(self):
        return self.title

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Žanras'

    def get_absolute_url(self):
        """Nurodo konkretaus aprašymo galinį adresą"""
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    """Modelis, aprašantis konkrečios knygos kopijos būseną"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unikalus ID knygos kopijai')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(name="due_back", verbose_name='Bus prieinama', null=True, blank=True)


    STATUS = (
        ('a', 'Administruojama'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='a',
        help_text='Statusas',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField('Vardas', max_length=100)
    last_name = models.CharField('Pavardė', max_length=100)

    def display_books(self):
        return ', '.join(book.title for book in self.books.all()[:3])

    display_books.short_description = 'Knygos'

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name} {self.first_name}'
