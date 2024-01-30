from django import forms
from . models import Typedocument

class TypedocumentForm(forms.ModelForm):
    class Meta:
        model = Typedocument
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name': 'Nombre',
            'acronyms': 'Acronimo',                 
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'acronyms': forms.TextInput(attrs={'placeholder': 'Ingresa el documento'}),        
        }