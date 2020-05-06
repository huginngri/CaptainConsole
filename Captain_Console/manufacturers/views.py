from django.shortcuts import render
from manufacturers.models import Manufacturer
from django.http import HttpResponse


def index(request):
    context = {'manufacturers': Manufacturer.objects.all().order_by('name')}
    return render(request, 'manufacturers/index.html', context)

def get_manufacturer_by_name(request, name):
    print("in this function now")
    manufacturer = {'manufacturer': Manufacturer.objects.get(name=name)}
    return render(request, 'manufacturers/manufacturer_details.html', manufacturer)