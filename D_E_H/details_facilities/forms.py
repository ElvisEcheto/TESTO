from django import forms
from . models import Details_Facilitie

class Details_FacilitieForm(forms.ModelForm):
    class Meta:
        model = Details_Facilitie
        fields = "__all__"
        exclude = ['status']
        labels = {
            'Lodging': 'Cabaña',
            'Facilitie': 'Comodidad',
                              
        }
        widgets = {
           
        }