# Imports
from django.urls import path
from . import views
# End Imports


# Config
app_name = 'mainapp'
urlpatterns = [
    path('', views.plug, name='plug'),
    path('testpage123/', views.index, name='index'),
    path('shop/', views.product_list, name='product_list'),
    path('shop/<slug:category_slug>/', views.category_detail, name='category_detail'),

]
# End Config
