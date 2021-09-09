from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInline (admin.TabularInline):
    model = OrderLineItem
    readonly_fields = (
        'lineitem_total',
    )


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    
    readonly_fields = (
        'order_number',
        'date',
        'order_total',
    )

    fields = (
        'order_number',
        'full_name',
        'email',
        'phone_number',
        'collection_location',
        'date',
        'order_total',
    )

    list_display = (
        'date',
        'order_number',
        'full_name',
        'collection_location',
        'order_total',
    )

    ordering = ('-date',)


class OrderLineItemAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'product',
        'item_size',
        'quantity',
        'lineitem_total'
    )

    ordering = ('product',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem, OrderLineItemAdmin)
