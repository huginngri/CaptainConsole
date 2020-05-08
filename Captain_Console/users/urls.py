from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views


urlpatterns = [
    # http://localhost:8000/products
    path('register', views.register, name="register"),
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name="logout"),
    path('profile', views.update_profile, name='profile'),
    path('profile/billing', views.update_billing, name='billing'),
    path('profile/payment', views.update_payment, name='payment')

]