from django.shortcuts import render
from users.models import Customer
from carts.models import Cart
from carts.models import CartDetails
from products.models import Product
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def add_to_cart(request):
    print(request.method)
    print(request)
    if request.method == 'POST':
        customer = Customer.objects.filter(user=request.user).first()
        cart = Cart.objects.filter(user=customer.id).first()
        product = Product.objects.get(id=request.POST['product_id'])
        cart_detail = CartDetails(cart = cart, product=product)
        cart_detail.save()
        return JsonResponse({'count': len(CartDetails.objects.filter(cart=cart.id))})
    elif request.method == "GET":
        customer = Customer.objects.filter(user=request.user).first()
        cart = Cart.objects.filter(user=customer.id).first()
        return JsonResponse({'count': len(CartDetails.objects.filter(cart=cart.id))})
    else:
        return JsonResponse({'error': 'Request failed'})

#def count_cart(request, id):
 #   if request.method == 'GET':
  #      customer = Customer.objects.filter(user=request.user).first()
   #     cart = Cart.objects.filter(user=customer.id).first()
    #    return JsonResponse({'count': len(CartDetails.objects.filter(cart=cart.id))})
    #else:
     #   return JsonResponse({'error': 'Request failed'})