from django.forms import ModelForm, widgets
from django import forms
from django_starfield import Stars

from products.models import Review


class ReviewForm(ModelForm):
    class Meta:
        stars = []

        for x in range(1,6):
            stars.append((x,"*"*x))
        stars = tuple(stars)
        model = Review
        exclude = ['id', 'customer', 'product']
        widgets = {
            'comment': widgets.TextInput(attrs={'class': 'form-control'}),
            'star': widgets.Select(choices=stars)
        }

