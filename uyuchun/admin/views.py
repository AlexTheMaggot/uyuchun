from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import AuthLoginForm, HeaderForm, IndexPageForm
from .models import Header, IndexPage
from mainapp.models import Category, SubCategory, Product, ProductImage
from mainapp.forms import CategoryForm, SubCategoryForm, ProductForm, ProductImageForm


class AuthLoginView(LoginView):
    template_name = 'admin/auth.html'
    form_class = AuthLoginForm
    success_url = reverse_lazy('admin:index')

    def get_success_url(self):
        return self.success_url


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('admin:login')


def index(request):
    if request.user.is_authenticated:
        template = 'admin/index.html'
        return render(request, template)
    else:
        return redirect('admin:login')


def content(request):
    if request.user.is_authenticated:
        template = 'admin/content.html'
        return render(request, template)
    else:
        return redirect('admin:login')


def content_header(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            context = {
                'header': Header.objects.first(),
            }
            template = 'admin/content_header.html'
            return render(request, template, context)
        elif request.method == 'POST':
            header = Header.objects.first()
            form = HeaderForm(request.POST, request.FILES, instance=header)
            if form.is_valid():
                form.save()
                return redirect('admin:content_header')
            else:
                return redirect('admin:error')
        else:
            return HttpResponse(status=403)
    else:
        return redirect('admin:login')


def catalog(request):
    if request.user.is_authenticated:
        template = 'admin/catalog.html'
        return render(request, template)
    else:
        return redirect('admin:login')


# Category
def category_list(request):
    if request.user.is_authenticated:
        context = {
            'categories': Category.objects.all()
        }
        template = 'admin/catalog/category_list.html'
        return render(request, template, context)
    else:
        return redirect('admin:login')


def category_create(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            template = 'admin/catalog/category_create.html'
            return render(request, template)
        elif request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin:category_list')
            else:
                return redirect('admin:error')
        else:
            return HttpResponse(status=403)
    else:
        return redirect('admin:login')


def category_update(request, category_id):
    if request.user.is_authenticated:
        category = Category.objects.get(id=category_id)
        if request.method == 'GET':
            context = {
                'category': category,
            }
            template = 'admin/catalog/category_update.html'
            return render(request, template, context)
        elif request.method == 'POST':
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                return redirect('admin:category_list')
            else:
                return redirect('admin:error')
        else:
            return HttpResponse(status=403)
    else:
        return redirect('admin:login')


def category_delete(request, category_id):
    if request.user.is_authenticated:
        category = Category.objects.get(id=category_id)
        category.delete()
        return redirect('admin:category_list')
    else:
        return redirect('admin:login')
# End Category


# SubCategory
def subcategory_list(request):
    if request.user.is_authenticated:
        context = {
            'subcategories': SubCategory.objects.all()
        }
        template = 'admin/catalog/subcategory_list.html'
        return render(request, template, context)
    else:
        return redirect('admin:login')


def subcategory_create(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            context = {
                'categories': Category.objects.all()
            }
            template = 'admin/catalog/subcategory_create.html'
            return render(request, template, context)
        elif request.method == 'POST':
            form = SubCategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin:subcategory_list')
            else:
                return redirect('admin:error')
        else:
            return HttpResponse(status=403)
    else:
        return redirect('admin:login')


def subcategory_update(request, subcategory_id):
    if request.user.is_authenticated:
        categories = Category.objects.all()
        subcategory = SubCategory.objects.get(id=subcategory_id)
        if request.method == 'GET':
            context = {
                'subcategory': subcategory,
                'categories': categories,
            }
            template = 'admin/catalog/subcategory_update.html'
            return render(request, template, context)
        elif request.method == 'POST':
            form = SubCategoryForm(request.POST, instance=subcategory)
            if form.is_valid():
                form.save()
                return redirect('admin:subcategory_list')
            else:
                return redirect('admin:error')
        else:
            return HttpResponse(status=403)
    else:
        return redirect('admin:login')


def subcategory_delete(request, subcategory_id):
    if request.user.is_authenticated:
        subcategory = SubCategory.objects.get(id=subcategory_id)
        subcategory.delete()
        return redirect('admin:subcategory_list')
    else:
        return redirect('admin:login')
# End SubCategory


# Product
def product_list(request):
    if request.user.is_authenticated:
        context = {
            'products': Product.objects.all()
        }
        template = 'admin/catalog/product_list.html'
        return render(request, template, context)
    else:
        return redirect('admin:login')


def product_create(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            context = {
                'subcategories': SubCategory.objects.all()
            }
            template = 'admin/catalog/product_create.html'
            return render(request, template, context)
        elif request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin:product_list')
            else:
                return redirect('admin:error')
        else:
            return HttpResponse(status=403)
    else:
        return redirect('admin:login')


def product_update(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        if request.method == 'GET':
            context = {
                'product': product,
                'subcategories': SubCategory.objects.all(),
            }
            template = 'admin/catalog/product_update.html'
            return render(request, template, context)
        elif request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('admin:product_list')
            else:
                return redirect('admin:error')
        else:
            return HttpResponse(status=403)
    else:
        return redirect('admin:login')


def product_delete(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        product.delete()
        return redirect('admin:product_list')
    else:
        return redirect('admin:login')


def product_image(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        if request.method == 'GET':
            template = 'admin/catalog/product_image.html'
            context = {
                'product': product,
            }
            return render(request, template, context)
        elif request.method == "POST":
            form = ProductImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('admin:product_image', product.id)
            else:
                return redirect('admin:error')
    else:
        return redirect('admin:login')


def product_image_delete(request, product_id, image_id):
    image = ProductImage.objects.get(id=image_id)
    image.delete()
    return redirect('admin:product_image', product_id)
# End Product


def pages(request):
    if request.user.is_authenticated:
        template = 'admin/pages.html'
        return render(request, template)
    else:
        return redirect('admin:login')


def pages_indexpage(request):
    if request.user.is_authenticated:
        indexpage = IndexPage.objects.first()
        if request.method == 'GET':
            template = 'admin/pages_indexpage.html'
            context = {
                'indexpage': indexpage,
            }
            return render(request, template, context)
        elif request.method == "POST":
            form = IndexPageForm(request.POST, request.FILES, instance=indexpage)
            if form.is_valid():
                form.save()
                return redirect('admin:pages_indexpage')
            else:
                return redirect('admin:error')
    else:
        return redirect('admin:login')


def error(request):
    if request.user.is_authenticated:
        template = 'admin/error.html'
        return render(request, template)
    else:
        return redirect('admin:login')