from django import forms
from . models import Costumer

class CostumerForm(forms.ModelForm):
    class Meta:
        model = Costumer
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name': 'Nombre',
            'document': 'Documento',
            'type_document': 'Tipo de documento',                       
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'document': forms.TextInput(attrs={'placeholder': 'Ingresa el documento'}),
            'type_document': forms.TextInput(attrs={'placeholder': 'Ingresa el tipo de documento'}),            
        }