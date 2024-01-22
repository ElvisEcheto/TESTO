from django import forms
from . models import Reserve

class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = "__all__"
        exclude = ['status']
        labels = {
            'Date_I': 'Fecha inicio',
            'Status_R ': 'Estado reserva',
            'Pay_T': 'Fecha de pago',     
            'Satisfaction':'satisfaccion',  
            'customer':'cliente',
            'lodging':'cabaña'               
        }
        widgets = {
            'Date_I': forms.DateInput(attrs={'type': 'date'}),
            'Status_R': forms.TextInput(attrs={'placeholder': 'Ingresa el estado de reserva'}),
            'Pay_T': forms.NumberInput(attrs={'placeholder': 'Ingresa el pago'}),    
            'Satisfaction': forms.NumberInput(attrs={'placeholder': 'Ingresa la satisfaccion'}),           
        }