from django import forms
from . models import Typelodging

class TypelodgingForm(forms.ModelForm):
    class Meta:
        model = Typelodging
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name': 'Nombre',                 
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el documento'}),        
        }