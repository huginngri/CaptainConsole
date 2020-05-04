from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/manufacturers
    path('', views.index, name="manufacturers-index"),
]