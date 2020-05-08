from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    #http://localhost:8000/carts
    path('', views.add_to_cart, name="add-cart"),
    #path('<int:id>', views.count_cart, name="count-cart"),
    #path('<int:id>', views.count_cart, name="view-cart"),
]