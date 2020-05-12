from django import forms

from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from django import forms

class RemoveUser(forms.Form):
    b = User.objects.all()
    k = []
    for x in b:

        k.append((x.username, x.username))
    username = forms.ChoiceField(widget=forms.Select, choices=k)
