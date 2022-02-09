from django.urls import path
from . import views

app_name = 'admin'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.AuthLoginView.as_view(), name='login'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),

    # Content
    path('content/', views.content, name='content'),
    path('content/header/', views.content_header, name='content_header'),
    # End Content

    # Catalog
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/categories/', views.category_list, name='category_list'),
    path('catalog/categories/add/', views.category_create, name='category_create'),
    path('catalog/categories/<int:category_id>/edit/', views.category_update, name='category_update'),
    path('catalog/categories/<int:category_id>/delete/', views.category_delete, name='category_delete'),
    path('catalog/subcategories/', views.subcategory_list, name='subcategory_list'),
    path('catalog/subcategories/add/', views.subcategory_create, name='subcategory_create'),
    path('catalog/subcategories/<int:subcategory_id>/edit/', views.subcategory_update, name='subcategory_update'),
    path('catalog/subcategories/<int:subcategory_id>/delete/', views.subcategory_delete, name='subcategory_delete'),
    path('catalog/products/', views.product_list, name='product_list'),
    path('catalog/products/add/', views.product_create, name='product_create'),
    path('catalog/products/<int:product_id>/edit/', views.product_update, name='product_update'),
    path('catalog/products/<int:product_id>/delete/', views.product_delete, name='product_delete'),
    path('catalog/products/<int:product_id>/images/', views.product_image, name='product_image'),
    path('catalog/products/<int:product_id>/images/<int:image_id>/delete/', views.product_image_delete, name='product_image_delete'),
    # End Catalog

    # Pages
    path('pages/', views.pages, name='pages'),
    path('pages/indexpage/', views.pages_indexpage, name='pages_indexpage'),
    # End Pages

    path('error/', views.error, name='error'),
]
