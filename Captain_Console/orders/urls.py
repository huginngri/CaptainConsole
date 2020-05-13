from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    #http://localhost:8000/carts
    path('checkout', views.checkout, name="checkout"),
    path('checkout/savebilling', views.save_billing, name="checkout-save-billing"),
    path('checkout/savepayment', views.save_payment, name="checkout-save-payment"),
    path('checkout/update/<int:order_id>', views.update_order, name="checkout-update"),
    path('checkout/overview', views.confirm_order, name="checkout-overview"),
    path('order_history', views.order_history, name="order-history"),
    path('can_review/<int:product_id>', views.can_review, name="order-history")
]