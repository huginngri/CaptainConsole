from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from error_and_success import cases
from manufacturers.forms.manufacturers_form import ManufacturerForm
from manufacturers.models import Manufacturer
from products.models import Product
from consoles.models import Console



def index(request):
    context = {'manufacturers': Manufacturer.objects.all().order_by('name'), }
    context = cases.get_profile(context, request)
    return render(request, 'manufacturers/index.html', context)

def get_manufacturer_by_name(request, name):
    manufacturer = Manufacturer.objects.get(name=name)
    context = {'manufacturer': manufacturer, 'products': list(Product.objects.filter(manufacturer=manufacturer.id)), 'consoles': Console.objects.filter(manufacturer=manufacturer.id)}
    context = cases.get_profile(context, request)
    return render(request, 'manufacturers/manufacturer_details.html', context)

@login_required()
def create_manufacturer(request):
    if request.user.is_superuser:
        context = {
            'form1': ManufacturerForm(),
        }
        context = cases.get_profile(context, request)
        if request.method == "POST":
            form1 = ManufacturerForm(data=request.POST)
            if form1.is_valid():
                form1.save()
                context = cases.success(context,'Created manufacturer')
                return render(request, 'manufacturers/create_manufacturer.html', context)
            else:
                context = cases.error(context, 'Something went wrong')
        return render(request, 'manufacturers/create_manufacturer.html', context)
    else:
        context = cases.get_profile(dict(), request)
        context = cases.front_page(context)
        context = cases.error(context, "You shall not pass")
        return render(request, 'products/frontpage.html', context)



