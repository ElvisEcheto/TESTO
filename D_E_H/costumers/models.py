from django.db import models

class Costumer(models.Model):
    name = models.CharField(max_length=255)
    document = models.CharField(max_length=20, unique=True)
    type_document = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name