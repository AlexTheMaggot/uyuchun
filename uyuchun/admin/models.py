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
    secondblock_first_link = models.CharField(max_length=200, null=True, blank=True)
    secondblock_second_first_title = models.CharField(max_length=200, null=True, blank=True)
    secondblock_second_second_title = models.CharField(max_length=200, null=True, blank=True)
    secondblock_second_subtitle = models.CharField(max_length=200, null=True, blank=True)
    secondblock_second_img = models.ImageField(upload_to='indexpage/', null=True, blank=True)
    secondblock_second_link = models.CharField(max_length=200, null=True, blank=True)
    secondblock_third_first_title = models.CharField(max_length=200, null=True, blank=True)
    secondblock_third_second_title = models.CharField(max_length=200, null=True, blank=True)
    secondblock_third_subtitle = models.CharField(max_length=200, null=True, blank=True)
    secondblock_third_img = models.ImageField(upload_to='indexpage/', null=True, blank=True)
    secondblock_third_link = models.CharField(max_length=200, null=True, blank=True)


class Footer(models.Model):
    logo = models.ImageField(upload_to='footer/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    copyright = models.CharField(max_length=200, null=True, blank=True)
