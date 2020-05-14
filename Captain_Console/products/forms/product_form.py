from django.forms import ModelForm, widgets

from products.models import Product


class ProductForm(ModelForm):
    class Meta:
        types = [
            ('Game', 'Game'),
            ('Console', 'Console'),
            ('Accessory', 'Accessory')
        ]
        model = Product
        exclude = ['id', 'rating', 'manufacturer']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'type': widgets.Select(attrs={'class': 'form-control'}, choices=types),
            'console_type': widgets.Select(attrs={'class': 'form-control'}),
            'on_sale': widgets.CheckboxInput(attrs={'class': 'form-control'}),
            'discount': widgets.NumberInput(attrs={'class': 'form-control'})
        }