from django.forms import ModelForm, widgets
from users.models import Payment


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id']
        widgets = {
            'card_holder': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '16','minlength':'16','size':'16'}),
            'exp_date': widgets.TextInput(attrs={'class': 'form-control'}),
            'cvc': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '4', 'minlength': '3', 'size': '3'}),
        }

