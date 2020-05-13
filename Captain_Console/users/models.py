from django.contrib.auth.models import User
from django.db import models


class Payment(models.Model):
    card_holder = models.CharField(max_length=255, null=True, blank=True)
    card_number = models.CharField(max_length=16, null=True, blank=True)
    exp_date = models.CharField(max_length=255, null=True, blank=True)
    cvc = models.CharField(max_length=4, null=True, blank=True)

class Billing(models.Model):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    street_name = models.CharField(max_length=255, null=True, blank=True)
    house_number = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    zip = models.CharField(max_length=255, null=True, blank=True)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.CharField(default="images/mario-bros-nintendo-nes.jpg", max_length=999)
    payment = models.ForeignKey(Payment, blank=True, null=True, on_delete=models.CASCADE)
    billing = models.ForeignKey(Billing,blank=True, null=True, on_delete=models.CASCADE)



