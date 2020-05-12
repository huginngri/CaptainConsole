from django.shortcuts import render, redirect

from manufacturers.forms.manufacturers_form import ManufacturerForm
from manufacturers.models import Manufacturer
from products.models import Product
from consoles.models import Console
from django.http import HttpResponse

from users.models import Customer


def index(request):
    context = {'manufacturers': Manufacturer.objects.all().order_by('name')}
    return render(request, 'manufacturers/index.html', context)

def get_manufacturer_by_name(request, name):
    manufacturer = Manufacturer.objects.get(name=name)
    profile = None
    if request.user.is_authenticated:
        profile = Customer.objects.get(user=request.user)
    context = {'manufacturer': manufacturer, 'products': list(Product.objects.filter(manufacturer=manufacturer.id)), 'consoles': Console.objects.filter(manufacturer=manufacturer.id), 'profile': profile}
    return render(request, 'manufacturers/manufacturer_details.html', context)

def create_manufacturer(request):
    if request.method == "POST":
        form1 = ManufacturerForm(data=request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('frontpage')
    return render(request, 'manufacturers/create_manufacturer.html', {
        'form1': ManufacturerForm()
    })