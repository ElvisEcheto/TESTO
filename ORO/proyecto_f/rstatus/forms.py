from django import forms
from . models import Rstatu


class RstatuForm(forms.ModelForm):
    class Meta:
        model = Rstatu
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name': 'Nombre',
            'description' : 'Descripcion',         
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre '}),
            'description': forms.TextInput(attrs={'placeholder': 'Ingrese la descripción'}),
        }