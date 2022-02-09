from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Header, IndexPage


class AuthLoginForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class HeaderForm(forms.ModelForm):
    class Meta:
        model = Header
        fields = ('logo', 'phone', 'instagram', 'address', 'worktime',)


class IndexPageForm(forms.ModelForm):
    class Meta:
        model = IndexPage
        fields = (
            'firstblock_img',
            'firstblock_title',
            'firstblock_subtitle',
            'firstblock_description',
            'secondblock_first_first_title',
            'secondblock_first_second_title',
            'secondblock_first_subtitle',
            'secondblock_first_img',
            'secondblock_second_first_title',
            'secondblock_second_second_title',
            'secondblock_second_subtitle',
            'secondblock_second_img',
            'secondblock_third_first_title',
            'secondblock_third_second_title',
            'secondblock_third_subtitle',
            'secondblock_third_img',
        )
