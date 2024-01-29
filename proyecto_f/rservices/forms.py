from django import forms
from . models import Rservice

from reservations.models import Reservation
from services.models import Service

class RserviceForm(forms.ModelForm):
    Reservation = forms.ModelChoiceField(queryset=Reservation.objects.filter(status=True).order_by('name'))
    Service = forms.ModelChoiceField(queryset=Service.objects.filter(status=True).order_by('name'))
    class Meta:
        model = Rservice
        fields = "__all__"
        exclude = ['status']
        labels = {
            'value': 'Valor',   
        }
        widgets = {
            'value': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio del libro'}),
        }