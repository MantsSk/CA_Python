from .models import GameReview
from django import forms


class GameReviewForm(forms.ModelForm):
    class Meta:
        model = GameReview
        fields = ('reviewer', 'game', 'content', 'rating')
        widgets = {'game': forms.HiddenInput(
        ), 'reviewer': forms.HiddenInput()}  # Task remove
