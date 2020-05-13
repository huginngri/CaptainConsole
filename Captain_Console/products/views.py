from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
import operator
from consoles.models import Console
from manufacturers.models import Manufacturer
from orders.models import Order, OrderProduct
from products.forms.product_form import ProductForm
from products.forms.image_form import ImageForm
from products.forms.review_form import ReviewForm
from products.models import Product, ProductImage, ProductHistory, Review
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from users.models import Customer

def frontpage(request):
    profile = None
    if request.user.is_authenticated:
        profile = Customer.objects.get(user=request.user)
    context = {'products': Product.objects.all().order_by('name'), 'profile': profile}
    return render(request, 'products/frontpage.html', context)

@login_required()
def recent_view(request):
    if request.user.is_authenticated:
        x = ProductHistory.objects.order_by('product','-id').distinct('product')
        x = ProductHistory.objects.filter(user=request.user, id__in=x).order_by('-id')[:5]
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
        print("in this if statement")
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

        # if len(products)==0:
            # print("in this fun")
            # response = redirect('order_history')
            # return response
        
        return JsonResponse({'data': products})

    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'products/index.html', context)

def get_product_by_id(request, id, consolename=None, name=None):
    the_product = get_object_or_404(Product, pk=id)
    reviews = Review.objects.filter(product=the_product)
    full_reviews = [{
        'star': x.star,
        'comment': x.comment,
        'id': x.id,
        'image': get_object_or_404(Customer, pk=x.customer_id).image,
        'name': get_object_or_404(Customer, pk=x.customer_id).user.username
    }for x in reviews]
    profile = None
    if request.user.is_authenticated:
        profile = Customer.objects.get(user=request.user)
    product = {'product': the_product, 'filter': 'none', 'comments': full_reviews, 'profile': profile}
    if request.user.is_authenticated:
        new_item_view = ProductHistory(user=request.user, product=the_product)
        new_item_view.save()
    return render(request, 'products/product_details.html', product)

@login_required()
def create_product(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form1 = ProductForm(data=request.POST)
            form2 = ImageForm(data=request.POST)
            if form1.is_valid() and form2.is_valid():
                the_cons = Console.objects.get(pk=form1.instance.console_type.id)
                form1.instance.manufacturer = Manufacturer.objects.get(pk=the_cons.manufacturer.id)
                form1.save()
                form2.instance.product = form1.instance
                form2.save()
                return redirect('products')
        return render(request, 'products/create_product.html', {
            'form1': ProductForm(),
            'form2': ImageForm()
        })

@login_required()
def update_product(request, id):

    if request.user.is_superuser:
        the_product = Product.objects.filter(pk=id).first()
        if request.method == "POST":
            form = ProductForm(data=request.POST,instance=the_product)
            if form.is_valid():
                the_cons = Console.objects.get(pk=form.instance.console_type.id)
                form.instance.manufacturer = Manufacturer.objects.get(pk=the_cons.manufacturer.id)
                form.save()
                return redirect('products')
        return render(request, 'products/update_product.html', {
            'form': ProductForm(instance=the_product)
        })

@login_required()
def delete_product(request, id):

    if request.user.is_superuser:
        the_product = Product.objects.filter(pk=id).first()
        the_product.delete()
        return render(request, 'products/delete_product.html', {
            'form': ProductForm(instance=the_product)
        })

@login_required()
def review_product(request, id):
    profile = Customer.objects.filter(user=request.user).first()
    product = Product.objects.filter(pk=id).first()
    order = Order.objects.filter(customer=profile)
    list_of_order_id = []
    for x in order:
        list_of_order_id.append(x.id)

    if len(Review.objects.filter(customer=profile, product=product))==0:
        if len(OrderProduct.objects.filter(order__in=list_of_order_id, product=product)) > 0:
            if request.method == "POST":
                form = ReviewForm(data=request.POST)
                form.instance.customer = profile
                form.instance.product = product
                form.save()
                print(product.rating)
                print(form.instance.star)
                number_of_rev = len(Review.objects.filter(product=product))
                product.rating = (product.rating*(number_of_rev-1)+form.instance.star)/(number_of_rev)
                product.save()
                return redirect('frontpage')
            return render(request, 'products/review_product.html', {
                'form': ReviewForm()
            })
        else:
            return render(request, 'products/frontpage.html',
                          {'profile': profile, 'error': True, 'message': 'You must have ordered the product to review'})
    else:

        return render(request, 'products/frontpage.html', {'profile': profile, 'error': True, 'message': 'You can only review each product once'})

def search_no_response(request):
    return render(request, 'products/product_search_error.html')
