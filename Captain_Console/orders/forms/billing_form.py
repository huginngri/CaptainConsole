from django.forms import ModelForm, widgets
from django_countries.data import  COUNTRIES
from orders.models import Billing, TemporaryBilling


class BillingFormOrder(ModelForm):
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

class BillingUpdateFormOrder(ModelForm):
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

class TemporaryBillingForm(ModelForm):
    class Meta:
        countries = []

        for x in tuple(COUNTRIES.values()):

            countries.append((x,x))
        countries = tuple(countries)
        model = TemporaryBilling
        exclude = ['id']
        widgets = {
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country' : widgets.Select(choices= countries),
            'zip': widgets.TextInput(attrs={'class': 'form-control'})
        }