from django.db import models
from costumers.models import Costumer  # Asegúrate de importar tu modelo Costumer correctamente

class Reservation(models.Model):
    daterr = models.DateField()
    datess = models.DateField()
    dateff = models.DateField()
    price = models.IntegerField()
    costumer = models.ForeignKey(Costumer, on_delete=models.DO_NOTHING, null=True)  # Permitir valores nulos
    rstatu = models.CharField(max_length=200, default='Reservado')
    
    def __str__(self):
        return str(self.id)  # Convertir el ID a cadena para evitar errores de tipo
