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

from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name="products"),
    path('recent', views.recent_view, name="recents"),
    path('search_no_response', views.search_no_response, name="search-no-response"),
    # http://localhost:8000/products/q?=name
    path('<int:id>', views.get_product_by_id, name="products-from-search"),
    path('<int:id>/update', views.update_product, name="update-product"),
    path('<int:id>/update_photos', views.update_product_photo, name="update-product-photos"),
    path('<int:id>/delete', views.delete_product, name="delete-product"),
    path('<int:id>/review', views.review_product, name='review-product'),

    # Admin create product
    path('create_product', views.create_product, name="create-product")
]