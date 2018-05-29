from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.ProductSize)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'size', 'price']
    list_filter = ['category', 'size', 'price']
    list_editable = ["price"]
admin.site.register(models.Product, ProductAdmin)
