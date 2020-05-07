from django.forms import ModelForm, widgets
from django_countries.data import  COUNTRIES
from users.models import Billing


class BillingForm(ModelForm):
    class Meta:
        countries = []

        for x in tuple(COUNTRIES.values()):

            countries.append((x,x))
        countries = tuple(countries)
        model = Billing
        exclude = ['id']
        widgets = {
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country' : widgets.Select(choices= countries),
            'zip': widgets.TextInput(attrs={'class': 'form-control'})
        }

