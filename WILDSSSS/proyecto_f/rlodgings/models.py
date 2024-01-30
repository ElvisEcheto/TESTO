from django.db import models

class Rlodging(models.Model):
    value= models.IntegerField()
    reservation = models.ForeignKey('reservations.Reservation', on_delete=models.DO_NOTHING)
    lodging = models.ForeignKey('lodgings.Lodging', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.value
