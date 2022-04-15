# Imports
from django.shortcuts import render, get_object_or_404
from admin.models import Header, IndexPage, Footer
from .models import Category, Product, SubCategory
from django.http import Http404, HttpResponseNotFound
# End Imports


def get_context():
    context = {
        'header': Header.objects.first(),
        'footer': Footer.objects.first(),
        'categories': Category.objects.all(),
    }
    return context


# Config
def plug(request):
    template = 'mainapp/plug.html'
    return render(request, template)


def index(request):
    context = get_context()
    context['indexpage'] = IndexPage.objects.first()
    template = 'mainapp/index.html'
    return render(request, template, context)


def product_list(request):
    context = get_context()
    context['products'] = Product.objects.filter(published=True)
    template = 'mainapp/product_list.html'
    return render(request, template, context)


def category_detail(request, category_slug):
    context = get_context()
    context['category_detail'] = get_object_or_404(Category, slug=category_slug)
    template = 'mainapp/category_detail.html'
    return render(request, template, context)


def subcategory_detail(request, category_slug, subcategory_slug):
    context = get_context()
    context['subcategory_detail'] = get_object_or_404(SubCategory, slug=subcategory_slug)
    template = 'mainapp/subcategory_detail.html'
    return render(request, template, context)


def product_detail(request, category_slug, subcategory_slug, product_slug):
    context = get_context()
    context['product'] = get_object_or_404(Product, slug=product_slug, published=True)
    template = 'mainapp/product_detail.html'
    return render(request, template, context)


def search(request):
    context = get_context()
    if request.GET['category'] == 'all':
        context['products'] = Product.objects.filter(name__icontains=str(request.GET['name']))
    else:
        context['products'] = Product.objects.filter(subcategory__category=int(request.GET['category'])).filter(name__icontains=str(request.GET['name']))
    template = 'mainapp/search.html'
    return render(request, template, context)
# End Config
