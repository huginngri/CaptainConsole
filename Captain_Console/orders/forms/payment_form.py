
from django.forms import ModelForm, widgets

from orders.models import Payment, TemporaryPayment





class PaymentFormOrder(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id']
        widgets = {
            'card_holder': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '16','minlength':'16','size':'16'}),
            'exp_date': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '5','minlength':'4'}),
            'cvc': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '4','minlength':'3'})
        }

class PaymentUpdateFormOrder(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id']
        widgets = {
            'card_holder': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '16','minlength':'16','size':'16'}),
            'exp_date': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '5','minlength':'4'}),
            'cvc': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '4','minlength':'3'})
        }


class TemporaryPaymentForm(ModelForm):
    class Meta:
        model = TemporaryPayment
        exclude = ['id']
        widgets = {
            'card_holder': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '16','minlength':'16','size':'16'}),
            'exp_date': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '5','minlength':'4'}),
            'cvc': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '4','minlength':'3'})
        }

