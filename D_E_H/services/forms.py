from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
        exclude = ['status']
        labels = {
            'Name': 'Nombre',
            'Price': 'Precio',                     
        }
        widgets = {
            'Name': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'Price': forms.TextInput(attrs={'placeholder': 'Ingresa el precio'}), 
        }