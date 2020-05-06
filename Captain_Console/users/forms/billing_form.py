from django.forms import ModelForm, widgets
from django_countries.data import  COUNTRIES
from users.models import Billing


class BillingForm(ModelForm):
    class Meta:
        model = Billing
        exclude = ['id']
        widgets = {
            'image' : widgets.TextInput(attrs={'class':'form-control'}),
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country' : widgets.Select(choices= tuple(COUNTRIES.values())),
            'zip': widgets.TextInput(attrs={'class': 'form-control'})
        }

