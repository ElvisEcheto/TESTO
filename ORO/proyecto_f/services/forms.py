from django import forms
from . models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
        exclude = ['status']
        labels = {
            'image': 'Imagen',
            'name': 'Nombre',
            'price': 'Precio',
            'description': 'Descripción',  
        }
        widgets = {
            'image': forms.FileInput(attrs={'placeholder': 'Ingrese la imagen del libro'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese el código del libro'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio del libro'}),  
            'description': forms.TextInput(attrs={'placeholder': 'Ingrese el código del libro'}),
        }
        