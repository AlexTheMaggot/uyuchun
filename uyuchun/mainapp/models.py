# Imports
from django.db import models
# End Imports


# Config
class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField()


class SubCategory(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL,
                                 related_name='subcategories')


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField()
    subcategory = models.ForeignKey(SubCategory, null=True, blank=True, on_delete=models.SET_NULL,
                                    related_name='products')
    price = models.BigIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class ProductImage(models.Model):
    img = models.ImageField(upload_to='products/', null=True, blank=True)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL, related_name='images')
# End Config
