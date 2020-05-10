from django.shortcuts import render, redirect

from manufacturers.forms.manufacturers_form import ManufacturerForm
from manufacturers.models import Manufacturer
from products.models import Product
from consoles.models import Console
from django.http import HttpResponse


def index(request):
    context = {'manufacturers': Manufacturer.objects.all().order_by('name')}
    return render(request, 'manufacturers/index.html', context)

def get_manufacturer_by_name(request, name):

    manufacturer = Manufacturer.objects.get(name=name)

    context = {'manufacturer': manufacturer, 'products': list(Product.objects.filter(manufacturer=manufacturer.id)), 'consoles': Console.objects.filter(manufacturer=manufacturer.id)}
    return render(request, 'manufacturers/manufacturer_details.html', context)

def create_manufacturer(request):
    if request.method == "POST":
        form1 = ManufacturerForm(data=request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('frontpage')
    return render(request, 'products/create_product.html', {
        'form1': ManufacturerForm()
    })