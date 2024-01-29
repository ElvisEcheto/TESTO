from django.db import models

class Reservation(models.Model):
    daterr = models.DateField()
    datess = models.DateField()
    dateff = models.DateField()
    value= models.IntegerField()
    costumer = models.ForeignKey('costumers.Costumer', on_delete=models.DO_NOTHING)
    rstatu = models.ForeignKey('rstatus.Rstatu', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.daterr