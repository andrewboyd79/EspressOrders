from django import forms
from .models import Product, Category, Type


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

        categories = Category.objects.all()
        types = Type.objects.all()
