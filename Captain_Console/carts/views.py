from django.contrib.auth.decorators import login_required
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
@login_required()
def add_or_count_cart(request):
    print(request.method)
    print(request)

    if request.method == 'POST':
        customer = Customer.objects.filter(user=request.user).first()
        cart = Cart.objects.filter(user=customer.id).first()
        product = Product.objects.get(id=request.POST['product_id'])
        cart_detail = CartDetails(cart=cart, product=product)
        cart_detail.save()
        return JsonResponse({'count': len(CartDetails.objects.filter(cart=cart.id))})
    elif request.method == 'GET':
        customer = Customer.objects.filter(user=request.user).first()
        cart = Cart.objects.filter(user=customer.id).first()
        return JsonResponse({'count': len(CartDetails.objects.filter(cart=cart.id))})
    else:
        return JsonResponse({'error': 'Request failed'})

@login_required()
def view_cart(request):
    customer = Customer.objects.filter(user=request.user).first()
    cart = Cart.objects.filter(user=customer.id).first()
    cart_details = CartDetails.objects.filter(cart=cart)
    products = []
    total = 0
    for cart_detail in cart_details:
        product = Product.objects.filter(id=cart_detail.product.id).first()
        products.append(product)
        total += product.price
    orders = Order.objects.filter(customer=customer)
    for order in orders:
        if order.confirmed == False:
            order_products = OrderProduct.objects.filter(order=order)
            for order_product in order_products:
                order_product.delete()
            order.delete()
    context = {'cart': cart, 'products': products, 'total_price': total, 'profile': customer}
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