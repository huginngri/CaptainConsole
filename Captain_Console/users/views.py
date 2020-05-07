from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
from users.forms.payment_form import PaymentForm
from users.forms.profile_form import ProfileForm
from users.forms.billing_form import BillingForm
from users.models import Customer


def register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'users/register.html', {
        'form' : UserCreationForm()
    })

def update(request):
    profile = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = ProfileForm(instance=profile, data= request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, "users/profile.html",{
        "form": ProfileForm(instance=profile)
    })

def update_billing(request):
    profile = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = BillingForm(data= request.POST)
        if form.is_valid():
            new_billing = form.save()
            profile.billing = new_billing
            profile.save()
            return redirect('profile')
    return render(request, "users/billing.html",{
        "form": BillingForm()
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