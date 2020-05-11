from django.shortcuts import render, redirect
from orders.forms.payment_form import PaymentFormOrder
from orders.forms.billing_form import BillingFormOrder
from users.forms.billing_form import BillingForm
from users.forms.payment_form import PaymentForm
from users.models import Customer
from django.forms.models import model_to_dict
from orders.models import Order
from orders.models import OrderProduct
from carts.models import Cart
from carts.models import CartDetails
from products.models import Product, ProductImage
from django.http import JsonResponse

# Create your views here.
def checkout(request):
    profile = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form_billing = BillingFormOrder(data=request.POST)
        form_payment = PaymentFormOrder(data=request.POST)
        if form_billing.is_valid() and form_payment.is_valid():
            #new_billing = form_billing.save()
            #new_payment = form_payment.save()
            return display_order(request, form_billing, form_payment)
    return render(request, "orders/checkout.html", {
        "form_billing": BillingFormOrder(instance=profile.billing),
        "form_payment": PaymentFormOrder(instance=profile.payment)
    })

def save_billing(request):
    profile = Customer.objects.filter(user=request.user).first()
    print('rétt')
    if request.method == "POST":
        form_billing = BillingForm(instance=profile.billing, data=request.POST)
        if form_billing.is_valid():
            new_billing = form_billing.save()
            profile.billing = new_billing
            profile.save()
            return redirect('checkout')
    return render(request, "orders/checkout.html", {
        "form_billing": BillingForm(instance=profile.billing),
        "form_payment": PaymentForm(instance=profile.payment, data=request.POST)
    })

def save_payment(request):
    profile = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form_payment = PaymentForm(instance=profile.payment, data=request.POST)
        if form_payment.is_valid():
            new_payment = form_payment.save()
            profile.payment = new_payment
            profile.save()
            return redirect('checkout')
    return render(request, "orders/checkout.html", {
        "form_billing": BillingForm(instance=profile.billing, data=request.POST),
        "form_payment": PaymentForm(instance=profile.payment)
    })

def display_order(request, form_billing, form_payment):
    profile = Customer.objects.filter(user=request.user).first()
    cart = Cart.objects.filter(user=profile.id).first()
    cart_details = CartDetails.objects.filter(cart=cart)
    products = []
    total = 0
    for cart_detail in cart_details:
        product = Product.objects.get(id=cart_detail.product_id)
        total += product.price
        products.append(product)
    context = {'billing': form_billing, 'payment': form_payment,
                        'products': products, 'total_price': total}
    return render(request, 'orders/order_review.html', context)

def create_order(request):
    profile = Customer.objects.filter(user=request.user).first()
    if request.method == 'POST':
        billing = request.POST['billing']
        payment = request.POST['payment']
        order = Order(customer=profile, billing=billing, payment=payment)
        order.save()
        for product in request.POST['products']:
            order_product = OrderProduct(order=order, product=product)
            order_product.save()
    return redirect('frontpage')
    