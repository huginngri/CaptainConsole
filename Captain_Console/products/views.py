from django.shortcuts import render, redirect

from products.forms.product_form import ProductForm
from products.forms.image_form import ImageForm
from products.models import Product
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def frontpage(request):

    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price,
            'rating': x.rating,
            'image': x.productimage_set.last().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})

    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'products/frontpage.html', context)

def index(request):

    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price,
            'rating': x.rating,
            'image': x.productimage_set.last.image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})

    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'products/index.html', context)

def get_product_by_id(request, id, consolename=None, name=None):
    product = {'product': get_object_or_404(Product, pk=id), 'filter': 'none'}
    return render(request, 'products/product_details.html', product)

def create_product(request):
    if request.method == "POST":
        form1 = ProductForm(data=request.POST)
        if form1.is_valid():
            form1.save()
            form2 = ImageForm(data=request.POST)
            form2.instance.product = form1.instance
            form2.save()
            return redirect('products')
    return render(request, 'products/create_product.html', {
        'form1': ProductForm(),
        'form2': ImageForm()
    })

def update_product(request, id):
    the_product = Product.objects.filter(pk=id).first()
    if request.method == "POST":
        form = ProductForm(data=request.POST,instance=the_product)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, 'products/update_product.html', {
        'form': ProductForm(instance=the_product)
    })

def delete_product(request, id):
    the_product = Product.objects.filter(pk=id).first()
    the_product.delete()
    return redirect('products')