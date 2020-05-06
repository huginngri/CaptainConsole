from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/manufacturers/:manufacturerName/consoles/
    path('', views.index, name="consoles-index"),
    path('<str:name>', views.get_console_by_name, name="consoles-product"),
]