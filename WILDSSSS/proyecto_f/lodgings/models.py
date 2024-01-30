from django.db import models

class Lodging(models.Model):
    image = models.ImageField(upload_to='static/lodgings_images', null=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    capacity= models.IntegerField()
    description = models.CharField(max_length=255)
    typelodging = models.ForeignKey('typelodgings.Typelodging', on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.image
