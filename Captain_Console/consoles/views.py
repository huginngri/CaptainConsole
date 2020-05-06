from django.shortcuts import render
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