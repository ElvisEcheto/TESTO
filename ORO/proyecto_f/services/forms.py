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
            'image': forms.FileInput(attrs={'placeholder': 'Ingrese la imagen del Servicio'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ejemplo: Limpieza de cuarto '}),
            'price': forms.NumberInput(attrs={'placeholder': 'Ejemplo: 20000'}),  
            'description': forms.TextInput(attrs={'placeholder': 'Ejemplo: diariamente se hace aseo..'}),
        }
        