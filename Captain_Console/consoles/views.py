from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from consoles.forms.console_form import ConsoleForm
from consoles.models import Console
from products.models import Product
from manufacturers.views import get_manufactorers_and_consoles_for_navbar
from django.http import HttpResponse

from users.models import Customer


def index(request):
    profile = None
    if request.user.is_authenticated:
        profile = Customer.objects.get(user=request.user)
    context = {'consoles': Console.objects.all().order_by('name'), 'profile':profile, 'nav': get_manufactorers_and_consoles_for_navbar() }
    return render(request, 'consoles/index.html', context)

def get_console_by_name(request, consolename, name=None):
    profile = None
    if request.user.is_authenticated:
        profile = Customer.objects.get(user=request.user)
    console = Console.objects.get(name=consolename)
    context = {'console': console, 'products': Product.objects.filter(console_type=console.id), 'filter': 'none', 'profile':profile, 'nav': get_manufactorers_and_consoles_for_navbar() }
    return render(request, 'consoles/console_details.html', context)

def get_consoles_by_name_console_names(request, consolename, name=None):
    profile = None
    if request.user.is_authenticated:
        profile = Customer.objects.get(user=request.user)
    console = Console.objects.get(name=consolename)
    context = {'console': console, 'products': Product.objects.filter(console_type=console.id, type='Console'), 'filter': 'Console', 'profile':profile, 'nav': get_manufactorers_and_consoles_for_navbar() }
    return render(request, 'consoles/console_details.html', context)

def get_games_by_name_console_names(request, consolename, name=None):
    profile = None
    if request.user.is_authenticated:
        profile = Customer.objects.get(user=request.user)
    console = Console.objects.get(name=consolename)
    context = {'console': console, 'products': Product.objects.filter(console_type=console.id, type='Game'), 'filter': 'Games', 'profile':profile, 'nav': get_manufactorers_and_consoles_for_navbar() }
    return render(request, 'consoles/console_details.html', context)

def get_accessories_by_name(request, consolename, name=None):
    profile = None
    if request.user.is_authenticated:
        profile = Customer.objects.get(user=request.user)
    console = Console.objects.get(name=consolename)
    context = {'console': console, 'products': Product.objects.filter(console_type=console.id, type='Accessory'), 'filter': 'Accessories', 'profile':profile, 'nav': get_manufactorers_and_consoles_for_navbar() }
    return render(request, 'consoles/console_details.html', context)

@login_required()
def create_console(request):
    profile = None
    if request.user.is_authenticated:
        profile = Customer.objects.get(user=request.user)
    if request.method == "POST":
        form1 = ConsoleForm(data=request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('frontpage')
    return render(request, 'consoles/create_console.html', {
        'form1': ConsoleForm(),
        'profile':profile,
        'nav': get_manufactorers_and_consoles_for_navbar()
    })

