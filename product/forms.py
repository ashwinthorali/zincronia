from django import forms
from .models import *
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method']        