from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CategoryForm, ProductForm
from .models import Category, Product, Shop


def main_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'new_main_page.html', context)


def category_sort(request, id):
    categories = Category.objects.all()
    products = Product.objects.filter(categories=id)
    context = {"products": products, "categories": categories}
    return render(request, 'categories_products.html', context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    shops = product.shop_set.all()
    # shop = Product.objects.filter(shop__products__in=1)
    context = {"product": product, "shops": shops}
    return render(request, 'product_detail.html', context)


def less_forms(request):
    categoris = Category.objects.all()
    prods = Product.objects.all()
    shops = Shop.objects.all()
    form = CategoryForm()
    context = {'categoris': categoris, 'prods': prods, 'shops': shops, 'form': form}
    return render(request, 'less_form.html', context)


def category_form(request):
    print(request.POST)
    Category.objects.create(name=request.POST.get('Category'))
    return redirect('new_site:less_forms')


def product_form(request):
    print(request.POST)
    Product.objects.create(title=request.POST.get('product_title'),
                           description=request.POST.get('product_description'),
                           price=request.POST.get('product_price'),
                           image=request.FILES.get('product_image'),
                           categories=Category.objects.get(name=request.POST.get('categories'))
                           )
    return redirect('new_site:less_forms')


def shop_form(request):
    print(request.POST)
    print(request.POST.getlist('prods'))
    a = Shop.objects.create(name=request.POST.get('name'),
                            city=request.POST.get('city'),
                            street=request.POST.get('street'),
                            )
    a.products.set('Product', request.POST.getlist('prods'))

    return redirect('new_site:less_forms')


def form_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    context = {'form': form}
    # return redirect('new_site:form_category')
    # context={'form':form}
    return render(request, "err.html", context)


def form_model(request):
    form = ProductForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, 'model_form.html', context)
