from django import forms
from . models import Facilitie

class FacilitieForm(forms.ModelForm):
    class Meta:
        model = Facilitie
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name': 'Nombre',                   
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),          
        }