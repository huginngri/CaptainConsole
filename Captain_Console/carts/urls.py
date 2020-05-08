from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [

    #http://localhost:8000/carts

    path('', views.add_or_count_cart, name="add-cart"),
    path('view/', views.view_cart, name="view-cart")
]