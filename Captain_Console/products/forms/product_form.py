from django.forms import ModelForm, widgets

from products.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-controll'}),
            'description': widgets.TextInput(attrs={'class': 'form-controll'}),
            'price': widgets.NumberInput(attrs={'class': 'form-controll'}),
            'rating': widgets.NumberInput(attrs={'class': 'form-controll'}),
            'type': widgets.TextInput(attrs={'class': 'form-controll'}),
            'manufacturer': widgets.Select(attrs={'class': 'form-controll'}),
            'console_type': widgets.Select(attrs={'class': 'form-controll'})
        }