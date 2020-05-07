from django.forms import ModelForm, widgets

from products.models import ProductImage


class ImageForm(ModelForm):
    class Meta:
        model = ProductImage
        exclude = ['id', 'product']
        widgets = {
            'image': widgets.TextInput(attrs={'class': 'form-control'})
        }