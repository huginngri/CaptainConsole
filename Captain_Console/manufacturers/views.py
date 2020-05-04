from django.shortcuts import render
from django.http import HttpResponse

# products = [
#     {'name': 'atari console', "price": 100},
#     {'name': 'atari controler', "price": 50}
# ]
# , context={'products': products}
# Create your views here.
def index(request):
    return render(request, "manufacturers/index.html")
