from django import forms
from . models import Payment

from reservations.models import Reservation

class PaymentForm(forms.ModelForm):
    reservation = forms.ModelChoiceField(queryset=Reservation.objects.filter(status=True).order_by('name'))
    class Meta:
        model = Payment
        fields = "__all__"
        exclude = ['status']
        labels = {
            'reservation': 'Reservacion',
            'date': 'Fecha',
            'value': 'Valor',
            'mathodpay': 'Metodo',
            'reservation' : 'Reserva',         
        }
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': 'Ingrese la imagen del libro'}),
            'value': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio del libro'}),
            'mathodpay': forms.TextInput(attrs={'placeholder': 'Ingrese el código del libro'}),
        }