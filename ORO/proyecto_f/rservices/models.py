from django.db import models

class Rservice(models.Model):
    price = models.IntegerField()
    reservation = models.ForeignKey('reservations.Reservation', on_delete=models.DO_NOTHING)
    service = models.ForeignKey('services.Service', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.value
