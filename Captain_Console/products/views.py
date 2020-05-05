from django.shortcuts import render
from products.models import Product
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def index(request):

    if 'search_filter' in request.GET:
        search_filter = request.GET('search-filter')
        products = [{
            'name': x.name,
            'description': x.name,
            'price': x.price,
            'rating': x.rating
            # 'console-type-id'
            # 'manufacturer-id'
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})

    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'products/index.html', context)

def get_product_by_id(request, id):
    product = {'product': get_object_or_404(Product, pk=id)}
    return render(request, 'products/product.html', product)

def create_product(request):
    if request.method == 'POST':
        print(1)
    else:
        print(2)
        # TODO: Instance new ProductCreateForm()