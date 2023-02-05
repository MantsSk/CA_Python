from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    name = models.CharField('TName', max_length=200,
                            help_text='Select or create game genre (FPS)')

    def __str__(self):
        return self.name


class Game(models.Model):
    """Modelis reprezentuoja žaidimą"""
    title = models.CharField('Name', max_length=200)
    publisher = models.ForeignKey(
        'Publisher', on_delete=models.SET_NULL, null=True, related_name='games')
    summary = models.TextField(
        _('Summary'), max_length=1000, help_text='Game description')
    genre = models.ManyToManyField(
        Genre, help_text='Select genres for games')
    cover = models.ImageField('Cover', upload_to='covers', null=True)

    def __str__(self):
        return f'{self.title}'

class Publisher(models.Model):
    """Model representing a publisher."""
    name = models.CharField('Name', max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'


class GameReview(models.Model):
    game = models.ForeignKey(
        Game, on_delete=models.SET_NULL, null=True, blank=True)
    reviewer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField('Rating', default=50, validators=[
        MinValueValidator(0), MaxValueValidator(100)])    
    content = models.TextField('Review Content', max_length=2000)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.game.title}'
