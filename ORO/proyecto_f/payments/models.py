from django.db import models

class Payment(models.Model):
    reservation = models.ForeignKey('reservations.Reservation', on_delete=models.DO_NOTHING)
    date = models.DateField()
    value = models.IntegerField()
    methodpay = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.reservation
