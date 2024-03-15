from django import forms
from . models import Payment


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = "__all__"
        exclude = ['status']
        labels = {
            'reservation': 'Reservacion',
            'date': 'Fecha',
            'value': 'Valor',
            'methodpay': 'Método',       
        }
        widgets = {
            'reserva': forms.TextInput(attrs={'placeholder': 'Reserva'}),
            'date': forms.DateInput(attrs={'type':'date'}),
            'value': forms.NumberInput(attrs={'placeholder': 'Ingrese el monto'}),
            'methodpay': forms.TextInput(attrs={'placeholder': 'Método'}),
        }