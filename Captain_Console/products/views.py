from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello from index view in products app')

def get_product_by_name(request, name):
    # TODO: select from database
    return HttpResponse(name)

def create_product(request):
    if request.method == 'POST':
        print(1)
    else:
        print(2)
        # TODO: Instance new ProductCreateForm()