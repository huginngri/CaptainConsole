from django.shortcuts import render, redirect
from users.forms.payment_form import PaymentForm
from users.forms.billing_form import BillingForm
from users.models import Customer
from users.models import Billing
from users.models import Payment
from orders.models import Order
from orders.models import OrderProduct
from carts.models import Cart
from carts.models import CartDetails
from products.models import Product

# Create your views here.
def checkout_billing(request):
    profile = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = BillingForm(instance=profile.billing, data=request.POST)
        if form.is_valid():
            new_billing = form.save()
            #profile.billing = new_billing
            #profile.save()
            return redirect('orders/payment_checkout.html', {'billing_id':  new_billing.id})
    return render(request, "orders/billing_checkout.html", {
        "form": BillingForm(instance=profile.billing)
    })

def save_billing(request):
    profile = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = BillingForm(instance=profile.billing, data=request.POST)
        if form.is_valid():
            new_billing = form.save()
            profile.billing = new_billing
            profile.save()
            return redirect('checkout-billing')
    return render(request, "orders/billing_checkout.html", {
        "form": BillingForm(instance=profile.billing)
    })

def checkout_payment(request):
    profile = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = PaymentForm(data=request.POST)
        if form.is_valid():
            new_payment = form.save()
            profile.payment = new_payment
            profile.save()
            return create_order(request, request.POST['billing_id'], new_payment.id)
    return render(request, "orders/payment_checkout.html", {
        "form": PaymentForm()
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