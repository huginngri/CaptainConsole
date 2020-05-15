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



@login_required()
def checkout(request, save=False, billing_saved=False, payment_saved=False):
    # this function is used to create payment and billing instances in the database
    # from forms that are provided in the requests. The parameters that are set to False
    # are used if the call to the method is called from the save functions below. They
    # are used to make sure that if billing or payment info is saved the request is not yet
    # rendered to the order_review because tthe review should only be displayed when the forms are
    # submitted
    profile = Customer.objects.filter(user=request.user).first()
    context = dict()
    if request.method == "POST" and save != True:
        # if the forms are submitted real billing and payment forms are initialized,
        # these forms allow no blank fields, different from the temporary forms.
        form_billing = BillingFormOrder(data=request.POST)
        form_payment = PaymentFormOrder(data=request.POST)

        if form_billing.is_valid() and form_payment.is_valid():
            # if the forms are valid in  comparison to the model classes they are
            # saved and sent to a function that displays an overview of the order
            new_billing = form_billing.save()
            new_payment = form_payment.save()
            return display_order(request, new_billing, new_payment)
        else:
            # if the forms are not valid temporary that allow blank fields forms with the users
            # input are initialized and the request is rendered to the sender again because
            # real forms can only be created if all fields are filled out
            context = cases.error(context, 'Please make sure that every field is filled out')
            context['form_billing'] = TemporaryBillingForm(data=request.POST)
            context['form_payment'] = TemporaryPaymentForm(data=request.POST)
            context = cases.get_profile(context, request)
            return render(request, "orders/checkout.html", context)
    elif save == True:
        # if the call to this function was from a svae function then the request is sennt back
        # to the user with the information that the info has been saved.
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
    # if the request is a GET request temporary forms are sent to the user but
    # the users saved information is used as data in the forms.
    context['form_billing'] = TemporaryBillingForm(instance=profile.billing)
    context['form_payment'] = TemporaryPaymentForm(instance=profile.payment)
    context = cases.get_profile(context, request)
    return render(request, "orders/checkout.html", context)


@login_required()
def save_billing(request):
    # this function is used to save billing info of a user.
    # A user billing form is initialized from the request and saved to
    # the users profile. Then the checkout function is called to return appropriate response
    # to the user
    profile = Customer.objects.filter(user=request.user).first()
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
    # this function is used to save payment info of a user.
    # A user payment form is initialized from the request and saved to
    # the users profile. Then the checkout function is called to return appropriate response
    # to the user
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
    # this function takes valid billing and payment information as input
    # and initializes and order instance with all the products in the users carts
    # and the provided billing and payment information. The order and products are
    # then sent back to the user
    profile = Customer.objects.filter(user=request.user).first()
    cart = Cart.objects.filter(user=profile.id).first()
    cart_details = CartDetails.objects.filter(cart=cart)
    order, products, total = create_order(profile, billing, payment, cart_details)
    context = {'order': order,'products': products, 'total_price': round(total,2)}
    context = cases.get_profile(context, request)
    return render(request, 'orders/order_review.html', context)

@login_required()
def create_order(profile, billing, payment, cart_details):
    # this function is used to help with the process of creating an order instance.
    # Loops through all the product in the cart and appends them to the order.
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
    return order, products, round(total,2)

@login_required()
def confirm_order(request):
    # this function is used to confirm an order. The order to confirm is provided in the request
    # and the order is set to true. Then the cart of the user is emptied because all items have been ordered.
    # The order is only served if there is enough stock of each product in the order, otherwise the order is deleted
    # and the cart remains the same, that is  the cart is not emptied
    profile = Customer.objects.filter(user=request.user).first()
    order = Order.objects.get(id=request.POST['order'])
    order.confirmed = True
    cart = Cart.objects.filter(user=profile.id).first()
    cart_details = CartDetails.objects.filter(cart=cart)
    for cart_detail in cart_details:
        product = Product.objects.get(id=cart_detail.product_id)
        quantity = cart_detail.quantity
        # if any product is out of stock, the order is cancelled
        if quantity > product.stock:
            order.delete()
            return JsonResponse({'message': 'out of stock', 'product': product.name, 'items_left': product.stock})
    # here, all products are in stock and the cart is emptied and stock modified
    for cart_detail in cart_details:
        product = Product.objects.get(id=cart_detail.product_id)
        quantity = cart_detail.quantity
        product.stock -= quantity
        product.save()
        cart_detail.delete()
    order.save()
    return JsonResponse({'message': 'success'})

@login_required()
def update_order(request, order_id):
    # this function is used to update billing and payment information of an order.
    # The order is provided in the request. The functionality is very similar to the
    # checkout function except that the saved payment and billing of the order are sent
    # to the user originally
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
            form_billing = TemporaryBillingForm(instance=billing)
            form_payment = TemporaryPaymentForm(instance=payment)
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


# Function that allows user to see his/hers order history
# and admin to see the order history of all users

@login_required()
def order_history(request):
    total = 0
    no_of_orders = 0
    total_no_of_orders = 0
    total_sold = 0

    # If the user is not a superuser only his/her order are displayed
    if not request.user.is_superuser:
        profile = Customer.objects.filter(user=request.user).first()
        # Orders that the customer has displayed are filtered out
        orders = Order.objects.filter(customer=profile)
        final_orders = []
        for order in orders:
            prods= []
            order_details = OrderProduct.objects.filter(order=order)
            for order_detail in order_details:
                product = Product.objects.get(id=order_detail.product_id)
                prods.append({'product': product, 'quantity': order_detail.quantity, 'image': ProductImage.objects.filter(product=product).first()})
                # The total amount spent is calculated based on whether the product was on discount price or not
                if product.on_sale == True:
                    total += (product.discount_price * order_detail.quantity)
                else:
                    total += (product.price * order_detail.quantity)
            # Order is given an attribute total and addres that are sent in the context to the HTML file
            order.total = str(round(total, 2)) + " $"
            order.address = order.billing.street_name + " " + order.billing.house_number + ", " + order.billing.zip + ", " + order.billing.country
            total = 0
            # Order is given an attribute confirmed
            if order.confirmed == True:
                order.status = "Done"
            else:
                order.status = "Open"
            no_of_orders += 1
            final_orders.append({'order': order, 'products': prods})
        context = {'orders': final_orders, 'total_orders': no_of_orders}
        context = cases.get_profile(context, request)
        return render(request, "orders/order_history_user.html", context)
    # If the user is a superuser (admin) all orders are displayed and the total that
    # has been sold is calculated and sent as an attribute with all_orders in the context
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
    # this function takes a request form a user and checks if the user may review the product
    # provided in the request. The user may only review it if he has ordered the product before.
    profile = Customer.objects.filter(user=request.user).first()
    orders = Order.objects.filter(customer=profile)
    product = Product.objects.get(id=product_id)
    for order in orders:
        order_products = OrderProduct.objects.filter(order=order)
        for order_product in order_products:
            if order_product.product == product:
                return JsonResponse({'can_review': True})
    return JsonResponse({'can_review': False})

