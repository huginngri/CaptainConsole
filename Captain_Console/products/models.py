from django.db import models
from manufacturers.models import Manufacturer
from users.models import Customer

# Create your models here.
<<<<<<< HEAD

=======
>>>>>>> 1c4e0834cf0d54759811b86fc0ae2c6e3d9a2c61
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
<<<<<<< HEAD
=======
    def __str__(self):
        return self.customer.name
>>>>>>> 1c4e0834cf0d54759811b86fc0ae2c6e3d9a2c61

class Search(models.Model):
    search_content = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
