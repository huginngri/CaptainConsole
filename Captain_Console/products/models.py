from django.contrib.auth.models import User
from django.db import models
from manufacturers.models import Manufacturer
from users.models import Customer
from consoles.models import Console

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    price = models.FloatField()
    console_type = models.ForeignKey(Console, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, null=True)
    rating = models.FloatField(default=0)
    stock = models.IntegerField(default=1)
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    star = models.IntegerField()
    comment = models.CharField(max_length=999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Search(models.Model):
    search_content = models.CharField(max_length=255)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

class ProductHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
