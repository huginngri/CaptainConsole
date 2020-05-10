from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [

    #http://localhost:8000/carts
    path('checkout/billing', views.checkout_billing, name="checkout-billing"),
    path('checkout/payment', views.checkout_payment, name="checkout-payment"),
    path('checkout/savebilling', views.save_billing, name="checkout-save-billing"),
    path('checkout/savepayment', views.save_payment, name="checkout-save-payment")
]