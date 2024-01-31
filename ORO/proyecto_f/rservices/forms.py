from django import forms
from . models import Rservice

class RserviceForm(forms.ModelForm):
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