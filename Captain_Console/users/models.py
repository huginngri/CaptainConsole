from django.contrib.auth.models import User
from django.db import models





class Payment(models.Model):
    card_holder = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    exp_date = models.CharField(max_length=255)
    cvc = models.CharField(max_length=255)

class Billing(models.Model):
    full_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.CharField(default="images/mario-bros-nintendo-nes.jpg", max_length=999)
    payment = models.ForeignKey(Payment, blank=True, null=True, on_delete=models.CASCADE)
    billing = models.ForeignKey(Billing,blank=True, null=True, on_delete=models.CASCADE)

