# Imports
from django.urls import path
from . import views
# End Imports


# Config
urlpatterns = [
    path('', views.index, name='index')
]
# End Config