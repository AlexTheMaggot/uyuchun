# Imports
from django.db import models
# End Imports


# Config
class Measure(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    short_name = models.CharField(max_length=200, null=True, blank=True)


class Specification(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    measure = models.ForeignKey(Measure, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='specifications')


class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField()


class SubCategory(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL,
                                 related_name='subcategories')
    img = models.ImageField(upload_to='subcategories/', null=True, blank=True)
    specifications = models.ManyToManyField(Specification, related_name='subcategories', null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField()
    subcategory = models.ForeignKey(SubCategory, null=True, blank=True, on_delete=models.SET_NULL,
                                    related_name='products')
    price = models.BigIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    available = models.BooleanField(default=False)
    published = models.BooleanField(default=False)


class ProductImage(models.Model):
    img = models.ImageField(upload_to='products/', null=True, blank=True)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL, related_name='images')


class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE,
                                related_name='productspecifications')
    specification = models.ForeignKey(Specification, null=True, blank=True, on_delete=models.CASCADE,
                                      related_name='productspecifications')
    value = models.CharField(max_length=200, null=True, blank=True)
# End Config
