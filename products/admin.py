from django.contrib import admin
from .models import Product, Category, Type

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'name',
        'brief_description',
        'starting_price',
        'category',
        'type'
    )

    ordering = ('id',)


class CategoryAdmin(admin.ModelAdmin):
    ordering = ('name',)


class TypeAdmin(admin.ModelAdmin):
    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
