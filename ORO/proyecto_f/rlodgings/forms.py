from django import forms
from . models import Rlodging

from reservations.models import Reservation
from lodgings.models import Lodging

class RlodgingForm(forms.ModelForm):
    Reservation = forms.ModelChoiceField(queryset=Reservation.objects.filter(status=True).order_by('name'))
    Lodging = forms.ModelChoiceField(queryset=Lodging.objects.filter(status=True).order_by('name'))
    class Meta:
        model = Reservation
        fields = "__all__"
        exclude = ['status']
        labels = {
            'value': 'Valor',   
        }
        widgets = {
            'value': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio del libro'}),
        }