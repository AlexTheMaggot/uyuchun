# Imports
from django.shortcuts import render
from admin.models import Header, IndexPage, Footer
from .models import Category
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
# End Config
