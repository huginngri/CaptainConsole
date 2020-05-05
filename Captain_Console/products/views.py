from django.shortcuts import render
from products.models import Product
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def index(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'products/index.html', context)

def get_product_by_name(request, name):
    product = {'product': get_object_or_404(Product, pk=name)}
    return render(request, 'products/product.html')

def create_product(request):
    if request.method == 'POST':
        print(1)
    else:
        print(2)
        # TODO: Instance new ProductCreateForm()