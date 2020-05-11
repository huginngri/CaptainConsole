from django.shortcuts import render, redirect
from orders.forms.payment_form import PaymentFormOrder
from orders.forms.billing_form import BillingFormOrder
from users.forms.billing_form import BillingForm
from users.forms.payment_form import PaymentForm
from users.models import Customer
from users.models import Billing
from users.models import Payment
from orders.models import Order
from orders.models import OrderProduct
from carts.models import Cart
from carts.models import CartDetails
from products.models import Product

# Create your views here.
def checkout(request):
    profile = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form_billing = BillingFormOrder(data=request.POST)
        form_payment = PaymentFormOrder(data=request.POST)
        if form_billing.is_valid() and form_payment.is_valid():
            new_billing = form_billing.save()
            new_payment = form_payment.save()
            return create_order(request, new_billing.id, new_payment.id)
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

def create_order(request, billing_id, payment_id):
    profile = Customer.objects.filter(user=request.user).first()
    cart = Cart.objects.filter(user=profile.id).first()
    cart_details = CartDetails.objects.filter(cart=cart)
    products = []
    for cart_detail in cart_details:
        products.append(Product.objects.filter(id=cart_detail.product.id).first())
    billing = Billing.objects.get(id=billing_id)
    payment = Payment.objects.get(id=payment_id)
    order = Order(customer=profile, billing=billing, payment=payment)
    order.save()
    for product in products:
        order_product = OrderProduct(order=order, product=product)
        order_product.save()
    return redirect('frontpage')