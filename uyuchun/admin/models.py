from django.db import models


class Header(models.Model):
    logo = models.ImageField(upload_to='mainpage/', null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    worktime = models.CharField(max_length=200, null=True, blank=True)


class IndexPage(models.Model):
    firstblock_img = models.ImageField(upload_to='indexpage/', null=True, blank=True)
    firstblock_title = models.CharField(max_length=200, null=True, blank=True)
    firstblock_subtitle = models.CharField(max_length=200, null=True, blank=True)
    firstblock_description = models.TextField(null=True, blank=True)
    secondblock_first_first_title = models.CharField(max_length=200, null=True, blank=True)
    secondblock_first_second_title = models.CharField(max_length=200, null=True, blank=True)
    secondblock_first_subtitle = models.CharField(max_length=200, null=True, blank=True)
    secondblock_first_img = models.ImageField(upload_to='indexpage/', null=True, blank=True)
    secondblock_second_first_title = models.CharField(max_length=200, null=True, blank=True)
    secondblock_second_second_title = models.CharField(max_length=200, null=True, blank=True)
    secondblock_second_subtitle = models.CharField(max_length=200, null=True, blank=True)
    secondblock_second_img = models.ImageField(upload_to='indexpage/', null=True, blank=True)
    secondblock_third_first_title = models.CharField(max_length=200, null=True, blank=True)
    secondblock_third_second_title = models.CharField(max_length=200, null=True, blank=True)
    secondblock_third_subtitle = models.CharField(max_length=200, null=True, blank=True)
    secondblock_third_img = models.ImageField(upload_to='indexpage/', null=True, blank=True)
