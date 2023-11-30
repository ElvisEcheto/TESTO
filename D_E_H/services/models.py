from django.db import models

class Services(models.Model):
    ID = models.IntegerField(primary_key=True,max_length=2)
    Name = models.CharField(max_length=20)
    Price = models.IntegerField()

    def __str__(self):
        return self.name