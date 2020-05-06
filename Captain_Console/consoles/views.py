from django.shortcuts import render, redirect

from consoles.forms.console_form import ConsoleForm
from consoles.models import Console
from products.models import Product
from django.http import HttpResponse


def index(request):
    context = {'consoles': Console.objects.all().order_by('name')}
    return render(request, 'consoles/index.html', context)

def get_console_by_name(request, name):
    console = Console.objects.get(name=name)
    context = {'console': console, 'products': Product.objects.filter(console_type=console.id)}
    return render(request, 'consoles/console_details.html', context)

def create_console(request):
    if request.method == "POST":
        form1 = ConsoleForm(data=request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('frontpage')
    return render(request, 'products/create_product.html', {
        'form1': ConsoleForm()
    })