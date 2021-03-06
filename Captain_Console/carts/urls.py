from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [

    #http://localhost:8000/carts

    path('', views.add_or_count_cart, name="add-cart"),
    path('view/', views.view_cart, name="view-cart"),
    path('<int:product_id>', views.remove_from_cart, name="remove-from-cart"),
    path('change_amount/<int:product_id>', views.change_quantity, name="remove-from-cart")
]