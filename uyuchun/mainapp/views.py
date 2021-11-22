# Imports
from django.shortcuts import render
# End Imports


# Config
def index(request):
    template = 'mainapp/index.html'
    return render(request, template)
# End Config