from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from manufacturers.forms.manufacturers_form import ManufacturerForm
from manufacturers.models import Manufacturer
from products.models import Product
from consoles.models import Console
from django.http import HttpResponse

from users.models import Customer


def index(request):
    profile = None
    if request.user.is_authenticated:
        profile = Customer.objects.get(user=request.user)
    context = {'manufacturers': Manufacturer.objects.all().order_by('name'), 'profile': profile, 'nav': get_manufactorers_and_consoles_for_navbar()}
    return render(request, 'manufacturers/index.html', context)

def get_manufacturer_by_name(request, name):
    manufacturer = Manufacturer.objects.get(name=name)
    profile = None
    if request.user.is_authenticated:
        profile = Customer.objects.get(user=request.user)
    context = {'manufacturer': manufacturer, 'products': list(Product.objects.filter(manufacturer=manufacturer.id)), 'consoles': Console.objects.filter(manufacturer=manufacturer.id), 'profile': profile, 'nav': get_manufactorers_and_consoles_for_navbar()}
    return render(request, 'manufacturers/manufacturer_details.html', context)

@login_required()
def create_manufacturer(request):
    if request.method == "POST":
        form1 = ManufacturerForm(data=request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('frontpage')
    return render(request, 'manufacturers/create_manufacturer.html', {
        'form1': ManufacturerForm(),
        'profile': Customer.objects.get(user=request.user),
        'nav': get_manufactorers_and_consoles_for_navbar()
    })

def get_manufactorers_and_consoles_for_navbar():
    manufacturers = Manufacturer.objects.all()
    nav_context = {}
    for manufacturer in manufacturers:
        consoles = Console.objects.filter(manufacturer=manufacturer)
        nav_context[manufacturer.name] = [console.name for console in consoles]
    return nav_context