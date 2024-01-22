from django import forms
from . models import Type_Lodging

class Type_LodgingForm(forms.ModelForm):
    class Meta:
        model = Type_Lodging
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name': 'Nombre',                    
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),        
        }