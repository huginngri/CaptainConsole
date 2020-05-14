from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from consoles.forms.console_form import ConsoleForm
from consoles.models import Console
from error_and_success import cases
from products.models import Product


def index(request):
    context = {'consoles': Console.objects.all().order_by('name')}
    context = cases.get_profile(context, request)
    return render(request, 'consoles/index.html', context)

def get_console_by_name(request, consolename, name=None):
    console = Console.objects.get(name=consolename)
    context = {'console': console, 'products': Product.objects.filter(console_type=console.id), 'filter': 'none' }
    context = cases.get_profile(context, request)
    return render(request, 'consoles/console_details.html', context)

def get_consoles_by_name_console_names(request, consolename, name=None):
    console = Console.objects.get(name=consolename)
    context = {'console': console, 'products': Product.objects.filter(console_type=console.id, type='console'), 'filter': 'Console'}
    context = cases.get_profile(context, request)
    return render(request, 'consoles/console_details.html', context)

def get_games_by_name_console_names(request, consolename, name=None):
    console = Console.objects.get(name=consolename)
    context = {'console': console, 'products': Product.objects.filter(console_type=console.id, type='game'), 'filter': 'Game'}
    context = cases.get_profile(context, request)
    return render(request, 'consoles/console_details.html', context)

def get_accessories_by_name(request, consolename, name=None):
    console = Console.objects.get(name=consolename)

    context = {'console': console, 'products': Product.objects.filter(console_type=console.id, type='accessory'),
               'filter': 'Accessory'}
    context = cases.get_profile(context, request)

    return render(request, 'consoles/console_details.html', context)

@login_required()
def create_console(request):
    if request.user.is_superuser:
        context = {'form1': ConsoleForm()}
        context = cases.get_profile(context, request)
        if request.method == "POST":
            form1 = ConsoleForm(data=request.POST)
            if form1.is_valid():
                form1.save()
                context = cases.success(context, 'Created console')
                return render(request, 'consoles/create_console.html', context)
            else:
                context = cases.error(context, 'Something went wrong')
        return render(request, 'consoles/create_console.html', context)
    else:
        context = cases.get_profile(dict(), request)
        context = cases.front_page(context)
        context = cases.error(context, "You shall not pass")
        return render(request, 'products/frontpage.html', context)

