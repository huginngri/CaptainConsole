from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [

    #http://localhost:8000/carts
    path('checkout/billing', views.checkout_billing, name="checkout-billing"),
    path('checkout/payment', views.checkout_payment, name="checkout-payment")

]