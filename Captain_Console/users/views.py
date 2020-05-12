from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

# Create your views here.
from carts.models import Cart
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
        'form' : UserCreationForm()
    })

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
        "form2": UserForm(instance=request.user)
    })

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
        "form": BillingForm(instance=profile.billing)
    })

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
        "form": PaymentForm()
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
        'form': form
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
                return redirect('main')
            else:
                pass
        ## Send some error messgae
    else:
        form = RemoveUser()
    context = {'form': form}
    return render(request, 'users/remove_user.html', context)

