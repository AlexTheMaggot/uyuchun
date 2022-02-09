# Imports
from django.urls import path
from . import views
# End Imports


# Config
app_name = 'mainapp'
urlpatterns = [
    path('', views.plug, name='plug'),
    path('testpage123/', views.index, name='index'),
]
# End Config
