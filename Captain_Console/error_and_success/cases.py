from consoles.models import Console
from manufacturers.models import Manufacturer

from orders.models import Order, OrderProduct
from products.models import Product
from users.models import Customer

#Sets the error message in the context and returns it
def error(context, message):
    context['error'] = True
    context['message'] = message
    return context

#Sets the profile if you are logged in and navbar in context and returns it
def get_profile(context, request):
    if request.user.is_authenticated:
        context['profile'] = Customer.objects.get(user=request.user)
    context['nav'] = get_manufactorers_and_consoles_for_navbar()
    return context

#Sets the success message in the context and returns it
def success(context, message):
    context['success'] = True
    context['message'] = message
    return context

#Gets the nav bar since it is interchangeable
def get_manufactorers_and_consoles_for_navbar():
    manufacturers = Manufacturer.objects.all()
    nav_context = {}
    for manufacturer in manufacturers:
        consoles = Console.objects.filter(manufacturer=manufacturer)
        nav_context[manufacturer.name] = [console.name for console in consoles]
    return nav_context

#This gets all the products that needs to be on the frontpage
def front_page(context):
    #For hot we need to get the last 20 orders, find the order details and for every order detail
    #add to a dict the quantity for the given product and finaly get a list of the 3 highest then it
    #is a simle sql query
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
    context['products_new'] = Product.objects.all().order_by('-id')[:3]
    context['products_hot'] = final_list
    context['products_deal'] = Product.objects.filter(on_sale=True).order_by('-discount')[:3]
    return context