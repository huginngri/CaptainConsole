from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from orders import views as orderviews


urlpatterns = [
    # http://localhost:8000/products
    path('register', views.register, name="register"),
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name="logout"),
    path('profile', views.update_profile, name='profile'),
    path('profile/billing', views.update_billing, name='billing'),
    path('profile/payment', views.update_payment, name='payment'),
    path('profile/change_password', views.change_password, name='change_password'),
    path('admin/profile/delete_user', views.delete_user, name='delete_user'),
    path('profile/order_history', orderviews.order_history, name="order-history"),
    path('profile/product_history', views.product_history, name='full-product-history')
]