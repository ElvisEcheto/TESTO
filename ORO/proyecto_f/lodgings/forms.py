from django import forms
from . models import Lodging

from typelodgings.models import Typelodging

class LodgingForm(forms.ModelForm):
    typelodging = forms.ModelChoiceField(queryset=Typelodging.objects.filter(status=True).order_by('name'))
    class Meta:
        model = Lodging
        fields = "__all__"
        exclude = ['status']
        labels = {
            'image': 'Imagen',
            'name': 'Nombre',
            'price': 'Precio',
            'capacity': 'Capacidad',
            'description': 'Descripción',
            'typelodging': 'Tipo cabaña',            
        }
        widgets = {
            'image': forms.FileInput(attrs={'placeholder': 'Ingrese la imagen del libro'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese el código del libro'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio del libro'}),  
            'capacity': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio del libro'}),
            'description': forms.TextInput(attrs={'placeholder': 'Ingrese el código del libro'}),
        }