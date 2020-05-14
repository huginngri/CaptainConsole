from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from error_and_success import cases
from orders.forms.payment_form import PaymentFormOrder, PaymentUpdateFormOrder, TemporaryPaymentForm
from orders.forms.billing_form import BillingFormOrder, BillingUpdateFormOrder, TemporaryBillingForm
from users.forms.billing_form import BillingForm
from users.forms.payment_form import PaymentForm
from orders.models import Billing
from orders.models import Payment
from users.models import Customer

from orders.models import Order
from orders.models import OrderProduct
from carts.models import Cart
from carts.models import CartDetails
from products.models import Product, ProductImage
from django.http import JsonResponse



# Create your views here.
@login_required()
def checkout(request, save=False, billing_saved=False, payment_saved=False):
    profile = Customer.objects.filter(user=request.user).first()
    context = dict()
    if request.method == "POST" and save != True:
        form_billing = BillingFormOrder(instance=profile.billing, data=request.POST)
        form_payment = PaymentFormOrder(instance=profile.billing, data=request.POST)
        if form_billing.is_valid() and form_payment.is_valid():
            new_billing = form_billing.save()
            new_payment = form_payment.save()
            return display_order(request, new_billing, new_payment)
        else:
            context = cases.error(context, 'Please make sure that billing and payment is valid')

    elif save == True:
        context = {
            "form_billing": TemporaryBillingForm(instance=profile.billing, data=request.POST),
            "form_payment": TemporaryPaymentForm(instance=profile.payment, data=request.POST),
        }
        context = cases.get_profile(context, request)
        if billing_saved:
            context["billing_saved"] = 'True'
            context['message'] = 'Billing information saved'
        if payment_saved:
            context["payment_saved"] = 'True'
            context['message'] = 'Payment information saved'
        return render(request, "orders/checkout.html", context)

    context['form_billing'] = TemporaryBillingForm(instance=profile.billing)
    context['form_payment'] = TemporaryPaymentForm(instance=profile.payment)
    context = cases.get_profile(context, request)
    return render(request, "orders/checkout.html",
        context
    )


@login_required()
def save_billing(request):
    profile = Customer.objects.filter(user=request.user).first()
    print('rétt')
    if request.method == "POST":
        form_billing = BillingForm(instance=profile.billing, data=request.POST)
        if form_billing.is_valid():
            new_billing = form_billing.save()
            profile.billing = new_billing
            profile.save()
            return checkout(request, save=True, billing_saved=True)
    context =  {"form_billing": TemporaryBillingForm(instance=profile.billing, data=request.POST),
        "form_payment": TemporaryPaymentForm(instance=profile.payment, data=request.POST)}
    context = cases.get_profile(context, request)
    return render(request, "orders/checkout.html", context)

@login_required()
def save_payment(request):
    profile = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form_payment = PaymentForm(instance=profile.payment, data=request.POST)
        if form_payment.is_valid():
            new_payment = form_payment.save()
            profile.payment = new_payment
            profile.save()
            return checkout(request, save=True, payment_saved=True)
    context = { "form_billing": TemporaryBillingForm(instance=profile.billing, data=request.POST),
        "form_payment": TemporaryPaymentForm(instance=profile.payment, data=request.POST),}
    context = cases.get_profile(context, request)
    return render(request, "orders/checkout.html", context)

@login_required()
def display_order(request, billing, payment):
    profile = Customer.objects.filter(user=request.user).first()
    cart = Cart.objects.filter(user=profile.id).first()
    cart_details = CartDetails.objects.filter(cart=cart)
    order, products, total = create_order(profile, billing, payment, cart_details)
    context = {'order': order,'products': products, 'total_price': total}
    context = cases.get_profile(context, request)
    return render(request, 'orders/order_review.html', context)

@login_required()
def create_order(profile, billing, payment, cart_details):
    order = Order(customer=profile, billing=billing, payment=payment)
    order.save()
    total = 0
    products = []
    for cart_detail in cart_details:
        product = Product.objects.get(id=cart_detail.product_id)
        products.append({'product': product, 'quantity': cart_detail.quantity})
        if product.on_sale == True:
            total += (product.discount_price * cart_detail.quantity)
        else:
            total += (product.price * cart_detail.quantity)
        order_product = OrderProduct(order=order, product=product, quantity=cart_detail.quantity)
        order_product.save()
    return order, products, total

@login_required()
def confirm_order(request):
    profile = Customer.objects.filter(user=request.user).first()
    order = Order.objects.get(id=request.POST['order'])
    order.confirmed = True
    cart = Cart.objects.filter(user=profile.id).first()
    cart_details = CartDetails.objects.filter(cart=cart)
    for cart_detail in cart_details:
        cart_detail.delete()
    order.save()
    return JsonResponse({'message': 'success'})

@login_required()
def update_order(request, order_id):
    profile = Customer.objects.filter(user=request.user).first()
    order = Order.objects.get(id=order_id)

    if order.customer == profile:
        billing = Billing.objects.get(id=order.billing_id)
        payment = Payment.objects.get(id=order.payment_id)
        if request.method == "POST":
            form_billing = BillingUpdateFormOrder(data=request.POST, instance=billing)
            form_payment = PaymentUpdateFormOrder(data=request.POST, instance=payment)
            if form_billing.is_valid() and form_payment.is_valid():
                form_billing.save()
                form_payment.save()
                return display_order(request, form_billing, form_payment)
        else:
            form_billing = BillingUpdateFormOrder(instance=billing)
            form_payment = PaymentUpdateFormOrder(instance=payment)
        context = {
            "form_billing": form_billing,
            "form_payment": form_payment}
        context = cases.get_profile(context, request)
        return render(request, "orders/checkout.html", context)
    else:
        context = cases.front_page(dict())
        context = cases.error(context, 'You shall not pass')
        context = cases.get_profile(context, request)
        return render(request, 'products/frontpage.html', context)


@login_required()
def order_history(request):
    total = 0
    no_of_orders = 0
    total_no_of_orders = 0
    total_sold = 0
    if not request.user.is_superuser:
        profile = Customer.objects.filter(user=request.user).first()
        orders = Order.objects.filter(customer=profile)
        final_orders = []
        for order in orders:
            prods= []
            order_details = OrderProduct.objects.filter(order=order)
            for order_detail in order_details:
                product = Product.objects.get(id=order_detail.product_id)
                prods.append({'product': product, 'quantity': order_detail.quantity, 'image': ProductImage.objects.filter(product=product).first()})
                if product.on_sale == True:
                    total += (product.discount_price * order_detail.quantity)
                else:
                    total += (product.price * order_detail.quantity)
            order.total = str(round(total, 2)) + " $"
            order.address = order.billing.street_name + " " + order.billing.house_number + ", " + order.billing.zip + ", " + order.billing.country
            total = 0
            if order.confirmed == True:
                order.status = "Done"
            else:
                order.status = "Open"
            no_of_orders += 1
            final_orders.append({'order': order, 'products': prods})
        context = {'orders': final_orders, 'total_orders': no_of_orders}
        context = cases.get_profile(context, request)
        return render(request, "orders/order_history_user.html", context)
    else:
        all_orders = Order.objects.all()
        for order in all_orders:
            order_details = OrderProduct.objects.filter(order=order)
            for order_detail in order_details:
                product = Product.objects.get(id=order_detail.product_id)
                if product.on_sale == True:
                    total += (product.discount_price * order_detail.quantity)
                else:
                    total += (product.price * order_detail.quantity)
            order.total = str(round(total, 2)) + " $"
            order.address = order.billing.street_name + " " + order.billing.house_number + ", " + order.billing.zip + ", " + order.billing.country
            total_sold += total
            total = 0
            total_no_of_orders += 1

        all_orders.total_sold = str(round(total_sold, 2))+ " $"
        all_orders.no = total_no_of_orders
        context = {'orders': all_orders}
        context = cases.get_profile(context, request)
        return render(request, "orders/order_history_admin.html", context)

@login_required()
def can_review(request, product_id):
    profile = Customer.objects.filter(user=request.user).first()
    orders = Order.objects.filter(customer=profile)
    product = Product.objects.get(id=product_id)
    for order in orders:
        order_products = OrderProduct.objects.filter(order=order)
        for order_product in order_products:
            if order_product.product == product:
                return JsonResponse({'can_review': True})
    return JsonResponse({'can_review': False})

