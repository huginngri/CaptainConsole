from django.db import models
from manufacturers.models import Manufacturer
from users.models import Customer

# Create your models here.
class ProductConsole(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    price = models.FloatField()
    console_type = models.ForeignKey(ProductConsole, on_delete=models.CASCADE)
    rating = models.FloatField()
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    star = models.FloatField()
    comment = models.CharField(max_length=999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.customer.name

class Search(models.Model):
    search_content = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
