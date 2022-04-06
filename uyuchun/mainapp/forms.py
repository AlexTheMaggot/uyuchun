from django import forms
from .models import Category, SubCategory, Product, ProductImage, Measure


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ('name', 'slug', 'category', 'img',)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'slug', 'subcategory', 'description', 'price', 'available', 'published')


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('img', 'product')


class MeasureForm(forms.ModelForm):
    class Meta:
        model = Measure
        fields = ('name', 'short_name')