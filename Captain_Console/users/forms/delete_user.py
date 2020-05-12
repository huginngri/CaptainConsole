
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets

class RemoveUser(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'password', 'last_login', 'groups', 'user_permissions', 'is_superuser', 'is_staff',
                   'is_active', 'date_joined', 'first_name', 'last_name', 'email']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
        }


