# DjangoImports
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
# End DjangoImports

# InternalImports
from .forms import AuthLoginForm, HeaderForm, IndexPageForm, FooterForm
from .models import Header, IndexPage, Footer
from mainapp.forms import CategoryForm, SubCategoryForm, ProductForm, ProductImageForm, MeasureForm, SpecificationForm
from mainapp.models import Category, SubCategory, Product, ProductImage, Measure, Specification, ProductSpecification
# End InternalImports


# Authentication
class AuthLoginView(LoginView):
    template_name = 'admin/auth.html'
    form_class = AuthLoginForm
    success_url = reverse_lazy('admin:index')

    def get_success_url(self):
        return self.success_url


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('admin:login')
# End Authentication


def index(request):
    if request.user.is_authenticated:
        template = 'admin/index.html'
        return render(request, template)
    else:
        return redirect('admin:login')


# Content
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


def content_footer(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            context = {
                'footer': Footer.objects.first(),
            }
            template = 'admin/content_footer.html'
            return render(request, template, context)
        elif request.method == 'POST':
            footer = Footer.objects.first()
            form = FooterForm(request.POST, request.FILES, instance=footer)
            if form.is_valid():
                form.save()
                return redirect('admin:content_footer')
            else:
                return redirect('admin:error')
        else:
            return HttpResponse(status=403)
    else:
        return redirect('admin:login')
# End Content


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
                'categories': Category.objects.all(),
                'specifications': Specification.objects.all(),
            }
            template = 'admin/catalog/subcategory_create.html'
            return render(request, template, context)
        elif request.method == 'POST':
            form = SubCategoryForm(request.POST, request.FILES)
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
        specifications = Specification.objects.all()
        if request.method == 'GET':
            context = {
                'subcategory': subcategory,
                'categories': categories,
                'specifications': specifications,
            }
            template = 'admin/catalog/subcategory_update.html'
            return render(request, template, context)
        elif request.method == 'POST':
            form = SubCategoryForm(request.POST, request.FILES, instance=subcategory)
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
                product = Product.objects.get(id=form.save().id)
                for item in product.subcategory.specifications.all():
                    new_spec = ProductSpecification(product=product, specification=item)
                    new_spec.save()
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


def handbook(request):
    if request.user.is_authenticated:
        template = 'admin/handbook.html'
        return render(request, template)
    else:
        return redirect('admin:login')


def measure_list(request):
    if request.user.is_authenticated:
        context = {
            'measures': Measure.objects.all()
        }
        template = 'admin/measure_list.html'
        return render(request, template, context)
    else:
        return redirect('admin:login')


def measure_create(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            template = 'admin/measure_create.html'
            return render(request, template)
        elif request.method == 'POST':
            form = MeasureForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin:measure_list')
            else:
                return redirect('admin:error')
        else:
            return HttpResponse(status=403)
    else:
        return redirect('admin:login')


def measure_update(request, measure_id):
    if request.user.is_authenticated:
        measure = Measure.objects.get(id=measure_id)
        if request.method == 'GET':
            context = {
                'measure': measure,
            }
            template = 'admin/measure_update.html'
            return render(request, template, context)
        elif request.method == 'POST':
            form = MeasureForm(request.POST, instance=measure)
            if form.is_valid():
                form.save()
                return redirect('admin:measure_list')
            else:
                return redirect('admin:error')
        else:
            return HttpResponse(status=403)
    else:
        return redirect('admin:login')


def measure_delete(request, measure_id):
    if request.user.is_authenticated:
        measure = Measure.objects.get(id=measure_id)
        measure.delete()
        return redirect('admin:measure_list')
    else:
        return redirect('admin:login')


def specification_list(request):
    if request.user.is_authenticated:
        context = {
            'specifications': Specification.objects.all()
        }
        template = 'admin/specification_list.html'
        return render(request, template, context)
    else:
        return redirect('admin:login')


def specification_create(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            context = {
                'measures': Measure.objects.all()
            }
            template = 'admin/specification_create.html'
            return render(request, template, context)
        elif request.method == 'POST':
            form = SpecificationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin:specification_list')
            else:
                return redirect('admin:error')
        else:
            return HttpResponse(status=403)
    else:
        return redirect('admin:login')


def specification_update(request, specification_id):
    if request.user.is_authenticated:
        specification = Specification.objects.get(id=specification_id)
        if request.method == 'GET':
            context = {
                'specification': specification,
                'measures': Measure.objects.all()
            }
            template = 'admin/specification_update.html'
            return render(request, template, context)
        elif request.method == 'POST':
            form = SpecificationForm(request.POST, instance=specification)
            if form.is_valid():
                form.save()
                return redirect('admin:specification_list')
            else:
                return redirect('admin:error')
        else:
            return HttpResponse(status=403)
    else:
        return redirect('admin:login')


def specification_delete(request, specification_id):
    if request.user.is_authenticated:
        specification = Specification.objects.get(id=specification_id)
        specification.delete()
        return redirect('admin:specification_list')
    else:
        return redirect('admin:login')


def error(request):
    if request.user.is_authenticated:
        template = 'admin/error.html'
        return render(request, template)
    else:
        return redirect('admin:login')
