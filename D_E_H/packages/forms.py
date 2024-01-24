from django import forms
from . models import Package

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name': 'Nombre',
            'price': 'Precio',
            'image': 'Imagen',
            'description': 'Descripcion',  
                                 
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'price': forms.TextInput(attrs={'placeholder': 'Ingresa el precio'}),
            'image': forms.FileInput(attrs={'placeholder': 'Ingresa la imagen'}), 
            'description': forms.TextInput(attrs={'placeholder': 'Ingresa descripcion'}),             
        }