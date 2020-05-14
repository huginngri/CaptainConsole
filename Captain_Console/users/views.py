
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

# Create your views here.
from carts.models import Cart
from products.models import ProductHistory, Product, ProductImage
from users.forms.payment_form import PaymentForm
from users.forms.profile_form import ProfileForm
from users.forms.billing_form import BillingForm
from users.forms.user_form import UserForm
from users.forms.delete_user import RemoveUser
from users.models import Customer
from error_and_success import cases
def register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            customer = Customer(user=form.instance)
            customer.save()
            cart = Cart(total=0, user=customer)
            cart.save()
            request.user = form.instance
            context = dict()
            context = cases.error(context, 'User created')
            return redirect('login')
    context = {'form': UserCreationForm()}
    context = cases.get_profile(context, request)
    return render(request, 'users/register.html', context)

@login_required()
def update_profile(request):
    profile = Customer.objects.filter(user=request.user).first()
    context = {
        "form1": ProfileForm(instance=profile),
        "form2": UserForm(instance=request.user),
    }
    context = cases.get_profile(context, request)
    if request.method == "POST":
        form1 = ProfileForm(instance=profile, data= request.POST)
        form2 = UserForm(instance=request.user, data= request.POST)
        if form1.is_valid():
            profile = form1.save(commit=False)
            profile.save()
            if form2.is_valid():
                request.user = form2.save(commit=False)
                request.user.save()
            context = {
                    "form1": ProfileForm(instance=profile),
                    "form2": UserForm(instance=request.user),
                }
            context = cases.success(context, 'Successfully updated profile')
            context = cases.get_profile(context, request)
            return render(request, "users/profile.html",context)
    return render(request, "users/profile.html", context)


@login_required()
def update_billing(request):
    profile = Customer.objects.filter(user=request.user).first()
    context = {
        "form": BillingForm(instance=profile.billing),
    }
    context = cases.get_profile(context, request)
    if request.method == "POST":
        form = BillingForm(instance=profile.billing, data=request.POST)
        if form.is_valid():
            new_billing = form.save()
            profile.billing = new_billing
            profile.save()

            context = cases.success(context, 'Updated billing')
            context['form'] = BillingForm(instance=profile.billing)
            return render(request,'users/billing.html', context)
    return render(request, "users/billing.html", context)


@login_required()
def update_payment(request):
    profile = Customer.objects.filter(user=request.user).first()
    context = {
        "form": PaymentForm(instance=profile.payment),
    }
    context = cases.get_profile(context, request)
    if request.method == "POST":
        form = PaymentForm(data= request.POST)
        if form.is_valid():
            new_payment = form.save()
            profile.payment = new_payment
            profile.save()
            context = cases.success(context, "Updated payment")
            context['form'] = PaymentForm(instance=profile.payment)
            return render(request, 'users/payment.html', context)
    return render(request, "users/payment.html", context)


@login_required()
def change_password(request):
    context = {
        'form': PasswordChangeForm(request.user),
    }
    context = cases.get_profile(context, request)
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed')
            return redirect('change_password')
        else:
            messages.error(request, 'Error')
    return render(request, 'users/change_password.html', context)


@login_required()
def delete_user(request):
    context = {'form': RemoveUser()}
    context = cases.get_profile(context, request)
    if not request.user.is_superuser:
        return messages.error(request, 'Error')
    if request.method == 'POST':
        form = RemoveUser(request.POST)
        if form.is_valid():
            rem = User.objects.get(username=form.cleaned_data['username'])
            if rem is not None:
                rem.delete()
                context = cases.success(context, 'User removed')
                return render(request,'users/user_removed.html', context)
            else:

                context = cases.error(context, "Something went wrong")
        else:
            context = cases.error(context, "Something went wrong")
    return render(request, 'users/remove_user.html', context)

@login_required()
def product_history(request):
    if request.user.is_authenticated:
        x = ProductHistory.objects.order_by('product','-id').distinct('product')
        x = ProductHistory.objects.filter(user=request.user, id__in=x).order_by('-id')
        the_products = []
        for y in x:
            the_products.append(get_object_or_404(Product, pk=y.product.id))
        recent_products = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price,
            'on_sale': x.on_sale,
            'discount': x.discount,
            'discount_price': x.discount_price,
            'rating': x.rating,
            'image': ProductImage.objects.filter(product=x.id).first().image
        } for x in the_products]

        context = cases.get_profile(dict(), request)
        context['products'] = recent_products
        return render(request, 'users/product_history.html', context)

