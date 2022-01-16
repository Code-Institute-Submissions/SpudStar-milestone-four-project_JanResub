from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Info
from .forms import ProductForm

# Create your views here.

def all_products(request):

    products = Info.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category']
            queries = Q(type1=categories) | Q(type2=categories)
            products = products.filter(queries)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No Pokemon name entered")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) 
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Info, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_product'))
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Info, pk=product_id)
    print(product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = ProductForm(instance=product)

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    print("TEST")
    print(product)
    print(product)
    print(product)
    print("TEST")
    return render(request, template, context)

def delete_product(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Info, pk=product_id)
    product.delete()
    return redirect(reverse('products'))
