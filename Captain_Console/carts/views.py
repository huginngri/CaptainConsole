from django.shortcuts import render, redirect
from users.models import Customer
from carts.models import Cart
from carts.models import CartDetails
from orders.models import Order, OrderProduct
from products.models import Product
from django.http import JsonResponse
from users.forms.payment_form import PaymentForm
from users.forms.billing_form import BillingForm


# Create your views here.
def add_or_count_cart(request):
    print(request.method)
    print(request)

    if request.method == 'POST':
        customer = Customer.objects.filter(user=request.user).first()
        cart = Cart.objects.filter(user=customer.id).first()
        product = Product.objects.get(id=request.POST['product_id'])
        cart_details = CartDetails.objects.filter(cart=cart, product=product)
        if len(cart_details) == 0:
            cart_detail = CartDetails(cart=cart, product=product)
        else:
            cart_detail = cart_details.first()
            cart_detail.quantity += 1
        cart_detail.save()
        return JsonResponse({'count': count_cart(customer, cart)})
    elif request.method == 'GET':
        customer = Customer.objects.filter(user=request.user).first()
        cart = Cart.objects.filter(user=customer.id).first()
        return JsonResponse({'count': count_cart(customer, cart)})
    else:
        return JsonResponse({'error': 'Request failed'})

def count_cart(customer, cart):
    count = 0
    for cart_detail in CartDetails.objects.filter(cart=cart):
        count += cart_detail.quantity
    return count

def view_cart(request):
    customer = Customer.objects.filter(user=request.user).first()
    cart = Cart.objects.filter(user=customer.id).first()
    cart_details = CartDetails.objects.filter(cart=cart)
    products = []
    total = 0
    for cart_detail in cart_details:
        product = Product.objects.filter(id=cart_detail.product.id).first()
        products.append({'product': product, 'quantity': cart_detail.quantity})
        total += (product.price * cart_detail.quantity)
    orders = Order.objects.filter(customer=customer)
    for order in orders:
        if order.confirmed == False:
            order_products = OrderProduct.objects.filter(order=order)
            for order_product in order_products:
                order_product.delete()
            order.delete()
    context = {'products': products, 'total_price': total}
    return render(request, 'carts/cart_details.html', context)

def remove_from_cart(request, product_id):
    customer = Customer.objects.filter(user=request.user).first()
    if request.method == 'DELETE':
        cart = Cart.objects.filter(user=customer.id).first()
        product = Product.objects.get(id=product_id)
        cart_detail = CartDetails.objects.filter(cart=cart, product=product).first()
        cart_detail.delete()
        return JsonResponse({'message': 'Product removed from cart'})
    return JsonResponse({'message': 'invalid request'})

def change_quantity(request, product_id):
    print('litla veislan')
    print(request.POST['new_amount'])
    customer = Customer.objects.filter(user=request.user).first()
    if request.method == 'POST':
        cart = Cart.objects.filter(user=customer.id).first()
        product = Product.objects.get(id=product_id)
        cart_detail = CartDetails.objects.filter(cart=cart, product=product).first()
        cart_details = CartDetails.objects.filter(cart=cart)
        total = 0
        if request.POST['new_amount'] == 0:
            remove_from_cart(request, product_id)
        else:
            cart_detail.quantity = request.POST['new_amount']
            cart_detail.save()
        for cart_detail in cart_details:
            total += product.price*cart_detail.quantity
        return JsonResponse({'total_price': total})
    return JsonResponse({'message': 'invalid request'})