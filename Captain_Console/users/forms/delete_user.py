from django import forms

class RemoveUser(forms.Form):
    username = forms.CharField()