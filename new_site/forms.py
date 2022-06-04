from django import forms
from django.core.exceptions import ValidationError

from new_site.models import Product


def valid_name(name):
    if name == "Johan":
        print(name)
    else:
        raise ValidationError('Имя не Johan')


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100, validators=[valid_name])
    password = forms.CharField(widget=forms.PasswordInput)
    price = forms.DecimalField(max_digits=8, decimal_places=2, required=False)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'price', 'categories']
