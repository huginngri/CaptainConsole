from django.db import models

from users.models import Customer
from products.models import Product

# Create your models here.

class Payment(models.Model):
    card_holder = models.CharField(max_length=255,null=True, blank=True)
    card_number = models.CharField(max_length=255,null=True, blank=True)
    exp_date = models.CharField(max_length=255,null=True, blank=True)
    cvc = models.CharField(max_length=255,null=True, blank=True)

class Billing(models.Model):
    full_name = models.CharField(max_length=255,null=True, blank=True)
    street_name = models.CharField(max_length=255,null=True, blank=True)
    house_number = models.CharField(max_length=255,null=True, blank=True)
    city = models.CharField(max_length=255,null=True, blank=True)
    country = models.CharField(max_length=255,null=True, blank=True)
    zip = models.CharField(max_length=255,null=True, blank=True)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

