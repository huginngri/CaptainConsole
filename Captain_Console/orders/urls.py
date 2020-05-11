from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [

    #http://localhost:8000/carts
    path('checkout', views.checkout, name="checkout"),
    path('checkout/savebilling', views.save_billing, name="checkout-save-billing"),
    path('checkout/savepayment', views.save_payment, name="checkout-save-payment"),
    path('checkout/overview', views.create_order, name="checkout-overview")
]