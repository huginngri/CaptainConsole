from django.forms import ModelForm, widgets
from users.models import Payment


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id']
        widgets = {
            'card_holder': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '16','minlength':'16'}),
            'exp_date': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '3','minlength':'4'}),
            'cvc': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '4', 'minlength': '3'}),
        }

