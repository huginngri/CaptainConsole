from django.db import models

from users.models import Customer
from products.models import Product

# Create your models here.

class TemporaryPayment(models.Model):
    card_holder = models.CharField(max_length=255,null=True, blank=True)
    card_number = models.CharField(max_length=16,null=True, blank=True)
    exp_date = models.CharField(max_length=5,null=True, blank=True)
    cvc = models.CharField(max_length=4,null=True, blank=True)

class TemporaryBilling(models.Model):
    full_name = models.CharField(max_length=255,null=True, blank=True)
    street_name = models.CharField(max_length=255,null=True, blank=True)
    house_number = models.CharField(max_length=255,null=True, blank=True)
    city = models.CharField(max_length=255,null=True, blank=True)
    country = models.CharField(max_length=255,null=True, blank=True)
    zip = models.CharField(max_length=255,null=True, blank=True)


class Payment(models.Model):
    card_holder = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    exp_date = models.CharField(max_length=5)
    cvc = models.CharField(max_length=4)

class Billing(models.Model):
    full_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

