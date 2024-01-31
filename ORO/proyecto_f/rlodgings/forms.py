from django import forms
from . models import Rlodging

class RlodgingForm(forms.ModelForm):
    class Meta:
        model = Rlodging
        fields = "__all__"
        exclude = ['status']
        labels = {
            'value': 'Valor',   
        }
        widgets = {
            'value': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio del libro'}),
        }