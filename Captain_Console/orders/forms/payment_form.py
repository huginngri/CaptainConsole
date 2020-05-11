from django.forms import ModelForm, widgets
from orders.models import Payment


class PaymentFormOrder(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id']
        widgets = {
            'card_holder': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'exp_date': widgets.TextInput(attrs={'class': 'form-control'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control'}),
        }

class PaymentUpdateFormOrder(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id']
        widgets = {
            'card_holder': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'exp_date': widgets.TextInput(attrs={'class': 'form-control'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control'}),
        }