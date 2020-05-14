from consoles.models import Console
from manufacturers.models import Manufacturer

from orders.models import Order, OrderProduct
from products.models import Product
from users.models import Customer


def error(context, message):
    context['error'] = True
    context['message'] = message

    return context

def get_profile(context, request):
    if request.user.is_authenticated:
        context['profile'] = Customer.objects.get(user=request.user)
    context['nav'] = get_manufactorers_and_consoles_for_navbar()
    return context

def success(context, message):
    context['success'] = True
    context['message'] = message
    return context

def get_manufactorers_and_consoles_for_navbar():
    manufacturers = Manufacturer.objects.all()
    nav_context = {}
    for manufacturer in manufacturers:
        consoles = Console.objects.filter(manufacturer=manufacturer)
        nav_context[manufacturer.name] = [console.name for console in consoles]
    return nav_context


def front_page(context):
    recent_orders = Order.objects.all().order_by('-id')[:20]
    kk = []
    for order in recent_orders:
        kk.append(OrderProduct.objects.filter(order=order))
    s = dict()
    for h in kk:
        for g in h:
            if g.product in s.keys():
                s[g.product] += g.quantity
            else:
                s[g.product] = g.quantity
    final_list = sorted(s, key=s.get, reverse=True)[:3]
    final_final_list = []
    for prod in final_list:
        final_final_list.append(prod.id)
    context['products_new'] = Product.objects.all().order_by('-id')[:3]
    context['products_hot'] = Product.objects.filter(id__in=final_final_list)
    context['products_deal'] = Product.objects.filter(on_sale=True).order_by('-discount')[:3]
    return context