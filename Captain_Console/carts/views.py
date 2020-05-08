from django.shortcuts import render
from users.models import Customer
from carts.models import Cart
from carts.models import CartDetails
from products.models import Product
from django.http import HttpResponse
from django.http import JsonResponse
from users.models import Billing
from users.models import Payment
from users.views import update_billing
from users.views import update_payment

# Create your views here.
def add_or_count_cart(request):
    print(request.method)
    print(request)

    if request.method == 'POST':
        customer = Customer.objects.filter(user=request.user).first()
        cart = Cart.objects.filter(user=customer.id).first()
        product = Product.objects.get(id=request.POST['product_id'])
        cart_detail = CartDetails(cart = cart, product=product)
        cart_detail.save()
        return JsonResponse({'count': len(CartDetails.objects.filter(cart=cart.id))})
    elif request.method == 'GET':
        customer = Customer.objects.filter(user=request.user).first()
        cart = Cart.objects.filter(user=customer.id).first()
        return JsonResponse({'count': len(CartDetails.objects.filter(cart=cart.id))})
    else:
        return JsonResponse({'error': 'Request failed'})


def view_cart(request):
    customer = Customer.objects.filter(user=request.user).first()
    cart = Cart.objects.filter(user=customer.id).first()
    cart_details = CartDetails.objects.filter(cart=cart)
    products = []
    for cart_detail in cart_details:
        products.append(Product.objects.filter(id=cart_detail.product.id).first())
    context = {'cart': cart, 'products': products}
    return render(request, 'carts/cart_details.html', context)

def checkout_billing(request):
    return update_billing(request)

def checkout_billing(request):
    return update_payment(request)