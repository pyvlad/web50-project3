from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'kind']
    list_filter = ['kind']
    list_editable = ['kind']
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.ProductSize)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'size', 'price']
    list_filter = ['category', 'size', 'price']
    list_editable = ["price"]
admin.site.register(models.Product, ProductAdmin)
