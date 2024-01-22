from django.db import models

class Details_Facilitie(models.Model):
    status = models.BooleanField(default=True)
    lodging = models.ForeignKey('lodgings.Lodging', on_delete=models.DO_NOTHING)
    facilitie = models.ForeignKey('facilities.Facilitie', on_delete=models.DO_NOTHING)
		
def __str__(self):
    return self.status