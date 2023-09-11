from .models import BookReview
from django import forms
from .models import Profile, Feedback
from django.contrib.auth.models import User


class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ('content', 'book', 'reviewer',)
        widgets = {'book': forms.HiddenInput(
        ), 'reviewer': forms.HiddenInput()}


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=255)
    comment = forms.CharField(widget=forms.Textarea)

class FeedbackModelForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'comment']