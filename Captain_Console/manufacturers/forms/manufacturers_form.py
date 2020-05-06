from django.forms import ModelForm, widgets

from manufacturers.models import Manufacturer


class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'}),

        }