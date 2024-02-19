from django import forms
from . models import Reservation

from costumers.models import Costumer

class ReservationForm(forms.ModelForm):
    Costumer = forms.ModelChoiceField(queryset=Costumer.objects.filter(status=True).order_by('name')),
    class Meta:
        model = Reservation
        fields = "__all__"
        exclude = ['status']
        labels = {
            'coder': 'codigo de reserva',
            'daterr': 'Fecha de Reserva',
            'datess': 'Fecha comienzo',
            'dateff': 'Fecha fin',
            'value': 'Valor',
            'costumer' : 'Cliente',
            'rstatu' : 'Estado Reserva',     
        }
        widgets = {
            'coder': forms.TextInput(attrs={'placeholder': 'Ejemplo: 22FF1'}),
            'daterr': forms.DateInput(attrs={'type':'date'}),
            'datess': forms.DateInput(attrs={'type':'date'}),
            'dateff': forms.DateInput(attrs={'type':'date'}),
            'value': forms.NumberInput(attrs={'placeholder': 'Ejemplo: 15000'}),
            'rstatu': forms.TextInput(attrs={'placeholder': 'Ejemplo: 22FF1'}),
        }