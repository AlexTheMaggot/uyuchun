from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ('name', 'slug', 'category', 'img', 'specifications')


class SubCategorySpecificationForm(forms.ModelForm):
    class Meta:
        model = SubCategorySpecification
        fields = ('specification', 'subcategory')


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


class SpecificationForm(forms.ModelForm):
    class Meta:
        model = Specification
        fields = ('name', 'measure')
