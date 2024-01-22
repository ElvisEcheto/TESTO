from django.db import models

class Lodging(models.Model):
    ID = models.IntegerField(primary_key=True,max_length=2)
    N_Beds = models.IntegerField(max_length=10)
    N_Bathrooms = models.IntegerField(max_length=5)
    Capacitance_T = models.IntegerField(max_legth=999999999)
    type_lodging = models.ForeignKey('type_lodgings.Type_Lodging', on_delete=models.DO_NOTHING)


def __str__(self):
        return self.title
