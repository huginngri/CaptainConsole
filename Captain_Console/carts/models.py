from django.db import models

# Create your models here.
from products.models import Product
from users.models import Customer


class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.FloatField()

class CartDetails(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
