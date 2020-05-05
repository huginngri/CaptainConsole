from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=999, blank=True)
    image = models.CharField(max_length=999, blank=True)
    def __str__(self):
        return self.name