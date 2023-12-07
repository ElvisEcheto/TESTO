from django.db import models

class Service(models.Model):
    Name = models.CharField(max_length=20)
    Price = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.Name