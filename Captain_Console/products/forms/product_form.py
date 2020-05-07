from django.forms import ModelForm, widgets

from products.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'rating': widgets.NumberInput(attrs={'class': 'form-control'}),
            'type': widgets.TextInput(attrs={'class': 'form-control'}),
            'manufacturer': widgets.Select(attrs={'class': 'form-control'}),
            'console_type': widgets.Select(attrs={'class': 'form-control'})
        }