from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from error_and_success import cases
from users.models import Customer
from carts.models import Cart
from carts.models import CartDetails
from orders.models import Order, OrderProduct
from products.models import Product
from django.http import JsonResponse



# Create your views here.
@login_required()
def add_or_count_cart(request):
    # this function responds to GET and POST requests to the url: /carts
    # it is used to add products to the cart (POST) and to display the size of the cart (GET)
    if request.method == 'POST':
        # If the method is POST we get the user that send the request and the corresponding shopping cart
        # If the cart already contains this product we raise the quantity in the cart by one, otherwise
        # we initialize a cart detail instance that connects the product to the cart
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
        # If the method is GET we get the user that send the request and the corresponding shopping cart
        # and return the size of the cart
        customer = Customer.objects.filter(user=request.user).first()
        cart = Cart.objects.filter(user=customer.id).first()
        return JsonResponse({'count': count_cart(customer, cart)})
    else:
        return JsonResponse({'error': 'invalid request'})


@login_required()
def count_cart(customer, cart):
    # this function calculates the size of a cart, looks at every cartdetail
    # and returns the sum of the quantity of each product in the cart
    count = 0
    for cart_detail in CartDetails.objects.filter(cart=cart):
        count += cart_detail.quantity
    return count

@login_required()
def view_cart(request):
    # This function takes a request from a registered user and returns a a list
    # of all the products in the user's cart along with the total price.
    customer = Customer.objects.filter(user=request.user).first()
    cart = Cart.objects.filter(user=customer.id).first()
    cart_details = CartDetails.objects.filter(cart=cart)
    products = []
    total = 0
    total_in_cart = 0
    for cart_detail in cart_details:
        product = Product.objects.filter(id=cart_detail.product.id).first()
        total_in_cart += 1
        products.append({'product': product, 'quantity': cart_detail.quantity})
        if product.on_sale == True:
            total += (product.discount_price * cart_detail.quantity)
        else:
            total += (product.price * cart_detail.quantity)
    orders = Order.objects.filter(customer=customer)
    # The user only has one cart and therefore all unconfirmed orders are deleted if
    # the user views his cart again without confirming an order, because if he is in
    # the cart the old order may be invalid and a new is created if he presses checkout
    for order in orders:
        if order.confirmed == False:
            order_products = OrderProduct.objects.filter(order=order)
            for order_product in order_products:
                order_product.delete()
            order.delete()

    context1 = {'products': products, 'total_price': round(total,2)}
    context1 = cases.get_profile(context1, request)
    context2 = cases.get_profile(dict(), request)


    if total_in_cart != 0:
        return render(request, 'carts/cart_details.html', context1)
    else:
        return render(request, 'carts/cart_details_empty.html', context2)

@login_required()
def remove_from_cart(request, product_id):
    # This function takes a DELETE request from a registered user and removes the product
    # supplied in the request from the user's cart. If the process is successful, the
    # new total price of the cart is returned
    customer = Customer.objects.filter(user=request.user).first()
    if request.method == 'DELETE':
        cart = Cart.objects.filter(user=customer.id).first()
        product = Product.objects.get(id=product_id)
        cart_detail = CartDetails.objects.filter(cart=cart, product=product).first()
        cart_detail.delete()
        return JsonResponse({'total_price': calc_price(cart)})
    return JsonResponse({'message': 'invalid request'})

def calc_price(cart):
    # this simple function finds all cart_detail instances connected to a cart
    # and returns the sum of the price of all the products in the cart
    total = 0
    cart_details = CartDetails.objects.filter(cart=cart)
    for cart_detail in cart_details:
        product = Product.objects.filter(id=cart_detail.product.id).first()
        # if the product is on sale, discount price is used
        if product.on_sale == True:
            total += (product.discount_price * cart_detail.quantity)
        else:
            total += (product.price * cart_detail.quantity)
    return round(total,2)

@login_required()
def change_quantity(request, product_id):
    # this function takes a request from a registered user and changes the
    # quantity of a given product in the user's cart. The new quantity is
    # provided in the request. Returns the new total price of the cart
    customer = Customer.objects.filter(user=request.user).first()
    if request.method == 'POST':
        cart = Cart.objects.filter(user=customer.id).first()
        product = Product.objects.get(id=product_id)
        cart_detail = CartDetails.objects.filter(cart=cart, product=product).first()
        # if the new amount is 0, remove the product from the cart
        if request.POST['new_amount'] == 0:
            remove_from_cart(request, product_id)
        else:
            cart_detail.quantity = request.POST['new_amount']
            cart_detail.save()
        return JsonResponse({'total_price': calc_price(cart)})
    return JsonResponse({'message': 'invalid request'})