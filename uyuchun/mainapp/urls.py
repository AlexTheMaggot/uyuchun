# Imports
from django.urls import path
from . import views
# End Imports


# Config
app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index')
]
# End Config