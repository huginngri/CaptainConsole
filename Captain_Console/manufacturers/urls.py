from django.urls import path, include
from . import views

urlpatterns = [
    #http://localhost:8000/manufacturers
    path('', views.index, name="manufacturers-index"),
    path('<str:name>', views.get_manufacturer_by_name, name="manufacturers-product"),
    path('<str:name>/consoles/', include('consoles.urls'))
]