from django.db import models

class Service(models.Model):
    image = models.ImageField(upload_to='static/services_images', null=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.image