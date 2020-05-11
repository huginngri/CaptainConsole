from django.urls import path
from . import views

urlpatterns = [
    path('create_console', views.create_console, name='create_console'),

]