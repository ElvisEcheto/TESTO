from django.db import models

class Clientes(models.Model):
    ID = models.IntegerField(primary_key=True,max_length=2)
    Full_Name = models.CharField(max_length=50, unique=True)
    Document_type = models.CharField(max_length=20)
    Document = models.IntegerField(max_length=20)

    def __str__(self):
        return self.name

# Create your models here.
