from django.db import models

class Lodging(models.Model):
    image = models.ImageField(upload_to='lodgings_images', null=True)
    N_Beds = models.IntegerField()
    N_Bathrooms = models.IntegerField()
    Capacitance_T = models.IntegerField()
    type_lodging = models.ForeignKey('type_lodgings.Type_Lodging', on_delete=models.DO_NOTHING)

    def __str__(self):
     return self.N_Beds