from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from error_and_success import cases
from manufacturers.forms.manufacturers_form import ManufacturerForm
from manufacturers.models import Manufacturer
from products.models import Product
from consoles.models import Console


#This is to get all manufacturers
def index(request):
    context = {'manufacturers': Manufacturer.objects.all().order_by('name'), }
    context = cases.get_profile(context, request)
    return render(request, 'manufacturers/index.html', context)

#This is to get all products for a specific manufacturer
def get_manufacturer_by_name(request, name):
    #Deals is a edge case and needs another process
    if name != 'Deals':
        manufacturer = Manufacturer.objects.get(name=name)
        context = {'manufacturer': manufacturer, 'products': list(Product.objects.filter(manufacturer=manufacturer.id)), 'consoles': Console.objects.filter(manufacturer=manufacturer.id)}
        context = cases.get_profile(context, request)
        return render(request, 'manufacturers/manufacturer_details.html', context)
    else:
        context = {'products': list(Product.objects.filter(on_sale=True))}
        context = cases.get_profile(context, request)
        return render(request, 'manufacturers/deals.html', context)


#This is for creating a manufacturer and works in the same way as console
@login_required()
def create_manufacturer(request):
    if request.user.is_superuser:
        context = {
            'form1': ManufacturerForm(),
        }
        if request.method == "POST":
            form1 = ManufacturerForm(data=request.POST)
            if form1.is_valid():
                form1.save()
                context = cases.get_profile(context, request)
                context = cases.success(context,'Created manufacturer')
                return render(request, 'manufacturers/create_manufacturer.html', context)
            else:
                context['form1'] = form1
                context = cases.get_profile(context, request)
                context = cases.error(context, 'Something went wrong')
        context = cases.get_profile(context, request)
        return render(request, 'manufacturers/create_manufacturer.html', context)
    else:
        context = cases.get_profile(dict(), request)
        context = cases.front_page(context)
        context = cases.error(context, "You shall not pass")
        return render(request, 'products/frontpage.html', context)



