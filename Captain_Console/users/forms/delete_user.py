
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from django import forms

class RemoveUser(forms.Form):
    username = forms.CharField()
