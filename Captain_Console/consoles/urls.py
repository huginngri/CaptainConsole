from django.urls import path
from . import views as v1
from products import views as v2



urlpatterns = [
    #http://localhost:8000/manufacturers/:manufacturerName/consoles/

    path('', v1.index, name="consoles-index"),
    path('<str:consolename>', v1.get_console_by_name, name="consoles-product"),
    path('<str:consolename>/consoles/', v1.get_consoles_by_name_console_names, name="consoles-consoles"),
    path('<str:consolename>/consoles/', v1.get_consoles_by_name_console_names, name="consoles-consoles"),
    path('<str:consolename>/consoles/<int:id>', v2.get_product_by_id, name="consoles-one-console"),
    path('<str:consolename>/games/', v1.get_games_by_name_console_names, name="consoles-games"),
    path('<str:consolename>/games/<int:id>', v2.get_product_by_id, name="consoles-one-game"),
    path('<str:consolename>/accessories/', v1.get_accessories_by_name, name="consoles-accessories"),
    path('<str:consolename>/accessories/<int:id>', v2.get_product_by_id, name="consoles-one-accessory")

]