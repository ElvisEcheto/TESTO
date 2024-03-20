from django import forms
from . models import Costumer

from typedocuments.models import Typedocument

class CostumerForm(forms.ModelForm):
    typedocument = forms.ModelChoiceField(queryset=Typedocument.objects.filter(status=True).order_by('name')),
    class Meta:
        model = Costumer
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name': 'Nombre',
            'document': 'Documento',
            'email': 'Correo',
            'typedocument': 'Tipo de documento',
            'phone': 'Teléfono',                  
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ejemplo: Andrés Felipe Gómez Sáez'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ejemplo: Andress@gmail.com'}),
            'document': forms.NumberInput(attrs={'placeholder': 'Ejemplo: 1081843749'}),  
            'phone': forms.NumberInput(attrs={'placeholder': 'Ejemplo: 30122254500'}),  
        }