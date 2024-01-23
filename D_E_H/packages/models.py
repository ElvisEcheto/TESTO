from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=20, unique=True)
    image = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name