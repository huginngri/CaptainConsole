from django.shortcuts import render
from users.models import Customer
from carts.models import Cart
from carts.models import CartDetails

# Create your views here.
def add_to_cart(request, product):
    customer = Customer.objects.filter(user=request.user).first()
    cart = Cart.objects.filter(user=customer.id)
    cart_detail = CartDetails(cart = cart, product=product)
    cart_detail.save()