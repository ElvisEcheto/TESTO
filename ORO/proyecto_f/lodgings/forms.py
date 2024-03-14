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
            'image': forms.FileInput(attrs={'placeholder': 'Ingrese la imagen'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio'}),  
            'capacity': forms.NumberInput(attrs={'placeholder': 'Ingrese la capacidad'}),
            'description': forms.TextInput(attrs={'placeholder': 'Ingrese la descripción'}),
        }