"""Captain_Console URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('products.urls2')),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('manufacturers/', include('manufacturers.urls')),
    path('users/', include('users.urls')),
    path('consoles/', include('consoles.urls2')),
    path('carts/', include('carts.urls')),
    path('orders/', include('orders.urls')),
    path('abuout_us', views.about, name="about"),

]
