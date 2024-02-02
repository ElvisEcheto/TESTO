from django import forms
from . models import Payment
from reservations.models import Reservation

class PaymentForm(forms.ModelForm):
    reservation = forms.ModelChoiceField(queryset=Reservation.objects.all()),
    class Meta:
        model = Payment
        fields = "__all__"
        exclude = ['status']
        labels = {
            'reservation': 'Reservacion',
            'date': 'Fecha',
            'value': 'Valor',
            'methodpay': 'Metodo',       
        }
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
            'value': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio del libro'}),
            'methodpay': forms.TextInput(attrs={'placeholder': 'Ingrese el código del libro'}),
        }