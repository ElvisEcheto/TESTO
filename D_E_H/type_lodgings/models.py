from django.db import models

class Type_Lodging(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
