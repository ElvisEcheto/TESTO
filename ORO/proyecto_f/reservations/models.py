from django.db import models

class Reservation(models.Model):
    coder = models.CharField(max_length=200)
    daterr = models.DateField()
    datess = models.DateField()
    dateff = models.DateField()
    price = models.IntegerField()
    costumer = models.ForeignKey('costumers.Costumer', on_delete=models.DO_NOTHING)
    rstatu = models.CharField(max_length=200,default='Reservado')
    
    def __str__(self):
        return self.coder