from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from consoles.models import Console
from manufacturers.models import Manufacturer
from products.forms.product_form import ProductForm
from products.forms.image_form import ImageForm
from products.models import Product, ProductImage, ProductHistory

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
            'image': ProductImage.objects.filter(product=x.id).first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'products/frontpage.html', context)

@login_required()
def recent_view(request):
    if request.user.is_authenticated:
        x = ProductHistory.objects.filter(user=request.user).order_by("-id")[:5]
        the_products = []
        for y in x:
            the_products.append(get_object_or_404(Product, pk=y.product.id))
        recent_products = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price,
            'rating': x.rating,
            'image': ProductImage.objects.filter(product=x.id).first().image
        } for x in the_products]
        return JsonResponse({'data': recent_products})

def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        list_of_manu = Manufacturer.objects.filter(name__icontains=search_filter)
        list_of_cons = Console.objects.filter(name__icontains=search_filter)
        manu_id = []
        cons_id = []
        for x in list_of_manu:
            manu_id.append(x.id)
        for y in list_of_cons:
            cons_id.append(y.id)
        products = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price,
            'image': ProductImage.objects.filter(product=x.id).first().image
        } for x in Product.objects.filter(Q(name__icontains=search_filter) | Q(console_type__in=cons_id )| Q(manufacturer__in=manu_id))]
        return JsonResponse({'data': products})

    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'products/index.html', context)

def get_product_by_id(request, id, consolename=None, name=None):
    the_product = get_object_or_404(Product, pk=id)
    product = {'product': the_product, 'filter': 'none'}
    if request.user.is_authenticated:
        new_item_view = ProductHistory(user=request.user, product=the_product)
        new_item_view.save()
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