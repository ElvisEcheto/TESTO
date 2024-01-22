from django.db import models

class Book(models.Model):
    status = models.BooleanField(default=True)
    reserve = models.ForeignKey('reserves.Reserve', on_delete=models.DO_NOTHING)
    service = models.ForeignKey('services.Service', on_delete=models.DO_NOTHING)

def __str__(self):
     return self.title
