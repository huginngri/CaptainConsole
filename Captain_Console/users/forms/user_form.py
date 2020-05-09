from django.contrib.auth.models import User
from django.forms import ModelForm, widgets




class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'password', 'last_login', 'groups', 'user_permissions', 'is_superuser', 'is_staff', 'is_active', 'date_joined']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'})
        }