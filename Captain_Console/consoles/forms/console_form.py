from django.forms import ModelForm, widgets

from consoles.models import Console


class ConsoleForm(ModelForm):
    class Meta:
        model = Console
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'manufacturer': widgets.Select(attrs={'class': 'form-control'})
        }