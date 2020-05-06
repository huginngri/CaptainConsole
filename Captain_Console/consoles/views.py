from django.shortcuts import render
from consoles.models import Console
from products.models import Product
from django.http import HttpResponse


def index(request):
    context = {'consoles': Console.objects.all().order_by('name')}
    return render(request, 'consoles/index.html', context)

def get_console_by_name(request, consolename, name=None):
    console = Console.objects.get(name=consolename)
    context = {'console': console, 'products': Product.objects.filter(console_type=console.id), 'filter': 'none'}
    return render(request, 'consoles/console_details.html', context)

def get_consoles_by_name_console_names(request, consolename, name=None):
    console = Console.objects.get(name=consolename)
    context = {'console': console, 'products': Product.objects.filter(console_type=console.id, type='console'), 'filter': 'console'}
    return render(request, 'consoles/console_details.html', context)

def get_games_by_name_console_names(request, consolename, name=None):
    console = Console.objects.get(name=consolename)
    context = {'console': console, 'products': Product.objects.filter(console_type=console.id, type='game'), 'filter': 'games'}
    return render(request, 'consoles/console_details.html', context)

def get_accessories_by_name(request, consolename, name=None):
    console = Console.objects.get(name=consolename)
    context = {'console': console, 'products': Product.objects.filter(console_type=console.id, type='accessory'), 'filter': 'accessories'}
    return render(request, 'consoles/console_details.html', context)