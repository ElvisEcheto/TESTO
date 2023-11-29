from django.db import models

class Cliente(models.Model):
    Full_Name = models.CharField(max_length=50)
    Document_type = models.CharField(max_length=20)
    Document = models.IntegerField(unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.Full_Name

# Create your models here.
