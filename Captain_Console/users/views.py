from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
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

def register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            customer = Customer(user=form.instance)
            customer.save()
            cart = Cart(total=0, user=customer)
            cart.save()
            return redirect('login')
    return render(request, 'users/register.html', {
        'form' : UserCreationForm(),
    })

@login_required()
def update_profile(request):
    profile = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form1 = ProfileForm(instance=profile, data= request.POST)
        form2 = UserForm(instance=request.user, data= request.POST)
        if form1.is_valid():
            profile = form1.save(commit=False)
            profile.save()
            if form2.is_valid():
                request.user = form2.save(commit=False)
                request.user.save()
            return redirect('profile')
    return render(request, "users/profile.html",{
        "form1": ProfileForm(instance=profile),
        "form2": UserForm(instance=request.user),
        "profile": profile
    })

@login_required()
def update_billing(request):
    profile = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = BillingForm(instance=profile.billing, data=request.POST)
        if form.is_valid():
            new_billing = form.save()
            profile.billing = new_billing
            profile.save()
            return redirect('profile')
    return render(request, "users/billing.html",{
        "form": BillingForm(instance=profile.billing),
        "profile": profile
    })

@login_required()
def update_payment(request):
    profile = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = PaymentForm(data= request.POST)
        if form.is_valid():
            new_payment = form.save()
            profile.payment = new_payment
            profile.save()
            return redirect('profile')
    return render(request, "users/payment.html",{

        "form": PaymentForm(),
        "profile": profile
    })

@login_required()
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed')
            return redirect('change_password')
        else:
            messages.error(request, 'Error')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form,
        'profile': Customer.objects.get(user=request.user)
    })

@login_required()
def delete_user(request):

    if not request.user.is_superuser:
        return messages.error(request, 'Error')
    if request.method == 'POST':
        form = RemoveUser(request.POST)

        if form.is_valid():
            rem = User.objects.get(username=form.cleaned_data['username'])
            if rem is not None:
                rem.delete()
                return render(request,'users/user_removed.html')
            else:
                pass
        ## Send some error messgae
    else:
        form = RemoveUser()
    
    context = {'form': form, 'profile': Customer.objects.get(user=request.user)}
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
            'dicount_price': x.discount_price,
            'rating': x.rating,
            'image': ProductImage.objects.filter(product=x.id).first().image
        } for x in the_products]
        return render(request, 'users/product_history.html', {'products': recent_products})

