from django import forms
from . models import Lodging

from type_lodgings.models import Type_Lodging

class LodgingForm(forms.ModelForm):
    type_lodging = forms.ModelChoiceField(queryset=Type_Lodging.objects.filter(status=True).
    order_by('name'))
    class Meta:
        model = Lodging
        fields = "__all__"
        exclude = ['status']
        labels = {
            'image' : 'Imagen de Cabaña', 
            'N_Beds': 'Numero camas',
            'N_Bathrooms': 'numero de baños',
            'Capacitance_T': 'capacidad personas',
            'type_lodging': 'Tipo cabaña',                      
        }
        widgets = {
            'image': forms.FileInput(attrs={'placeholder': 'Ingrese el archivo'}),   
            'N_Beds': forms.NumberInput(attrs={'placeholder': 'Ingresa el numero de camas'}),
            'N_Bathrooms': forms.NumberInput(attrs={'placeholder': 'Ingresa el numero de baños'}),
            'Capacitance_T': forms.NumberInput(attrs={'placeholder': 'Ingresa la capacidad de personas'}),       
        }