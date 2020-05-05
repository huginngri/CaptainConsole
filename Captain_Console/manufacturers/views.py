from django.shortcuts import render
from manufacturers.models import Manufacturer
from products.models import Product
from django.http import HttpResponse


def index(request):
    context = {'manufacturers': Manufacturer.objects.all().order_by('name')}
    return render(request, 'manufacturers/index.html', context)

def get_manufacturer_by_name(request, name):
    manufacturer = Manufacturer.objects.get(name=name)
    context = {'manufacturer': manufacturer, 'products': Product.objects.filter(manufacturer=manufacturer.id)}
    return render(request, 'manufacturers/manufacturer_details.html', context)
