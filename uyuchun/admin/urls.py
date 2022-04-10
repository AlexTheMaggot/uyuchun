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
    path('content/footer/', views.content_footer, name='content_footer'),
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
    path('catalog/products/<int:product_id>/images/<int:image_id>/delete/', views.product_image_delete,
         name='product_image_delete'),
    path('catalog/products/<int:product_id>/specifications/', views.product_specifications,
         name='product_specifications'),
    # End Catalog

    # Handbook
    path('handbook/', views.handbook, name='handbook'),
    path('handbook/measures/', views.measure_list, name='measure_list'),
    path('handbook/measures/add/', views.measure_create, name='measure_create'),
    path('handbook/measures/<int:measure_id>/edit/', views.measure_update, name='measure_update'),
    path('handbook/measures/<int:measure_id>/delete/', views.measure_delete, name='measure_delete'),
    path('handbook/specifications/', views.specification_list, name='specification_list'),
    path('handbook/specifications/add/', views.specification_create, name='specification_create'),
    path('handbook/specifications/<int:specification_id>/edit/', views.specification_update,
         name='specification_update'),
    path('handbook/specifications/<int:specification_id>/delete/', views.specification_delete,
         name='specification_delete'),
    # End Handbook




    # Pages
    path('pages/', views.pages, name='pages'),
    path('pages/indexpage/', views.pages_indexpage, name='pages_indexpage'),
    # End Pages

    path('error/', views.error, name='error'),
]
