from django import forms
from .models import products


class ProductForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ('Product_Name', 'Price', 'Description')
