from django import forms 
from .models import *
from dataclasses import fields

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'