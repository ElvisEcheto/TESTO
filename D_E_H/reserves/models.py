from django.db import models

class Reserve(models.Model):
    Date_I = models.DateField(max_length=30)
    Status_R = models.CharField(max_length=255)
    Pay_T = models.IntegerField()
    Satisfaction = models.CharField(max_length=2000)
    lodging = models.IntegerField()
    costumer =  models.IntegerField()
   
def __str__(self):
        return self.Date_I
