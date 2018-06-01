from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'kind']
    list_filter = ['kind']
    list_editable = ['kind']

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']

@admin.register(models.MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'get_category', 'size', 'price']
    list_filter = ['product__category', 'size']
    list_editable = ['price']
    def get_category(self, obj):
        return obj.product.category
    get_category.short_description = 'Category'
    get_category.admin_order_field = 'product__category'


# class SelectedItemInline(admin.StackedInline):
#     model = models.SelectedItem
#     extra = 1
#
# @admin.register(models.Selection)
# class SelectionAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', '__str__', 'category']
#     def category(self, obj):
#         return obj.items.first().product.category
#     inlines = [SelectedItemInline]
#
# @admin.register(models.SelectedItem)
# class SelectedItemAdmin(admin.ModelAdmin):
#     list_display = ['item', 'get_user', 'get_selection_id', 'get_category']
#     def get_user(self, obj):
#         return obj.selection.user
#     def get_selection_id(self, obj):
#         return obj.selection.id
#     def get_category(self, obj):
#         return obj.item.product.category.kind


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_user', 'contents', 'created', 'finished']
    list_editable = ['finished']
    list_filter = ['finished']
    filter_vertical = ('selections',)
    def get_user(self, obj):
        return obj.selections.first().user
    def contents(self, obj):
        return mark_safe("<br>".join([str(i) for i in obj.selections.all()]))
