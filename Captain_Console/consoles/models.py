from django.db import models
from manufacturers.models import Manufacturer

# Create your models here.

class Console(models.Model):
    name = models.CharField(max_length=255, unique=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    def __str__(self):
        return self.name