from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'kind']
    list_filter = ['kind']
    list_editable = ['kind']
admin.site.register(models.Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
admin.site.register(models.Product, ProductAdmin)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'get_category', 'size', 'price']
    list_filter = ['product__category', 'size']
    list_editable = ['price']

    def get_category(self, obj):
        return obj.product.category
    get_category.short_description = 'Category'
    get_category.admin_order_field = 'product__category'

admin.site.register(models.MenuItem, MenuItemAdmin)
