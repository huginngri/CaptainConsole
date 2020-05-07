from django.forms import ModelForm, widgets

from users.models import Customer


class ProfileForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ['id', 'user', 'billing', 'payment']
        widgets = {

            'image': widgets.TextInput(attrs={'class': 'form-control'})

        }