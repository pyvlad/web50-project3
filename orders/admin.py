from django.contrib import admin
from . import models

# Register your models here.
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['title', 'kind', "size", "toppings_number", "price"]
    list_filter = ['kind', "size", "toppings_number", "price"]
    list_editable = ["price"]
admin.site.register(models.Pizza, PizzaAdmin)
admin.site.register(models.PizzaTopping)

class SubAdmin(admin.ModelAdmin):
    list_display = ['title', "size", "price"]
    list_filter = ["size", "price"]
    list_editable = ["price"]
admin.site.register(models.Sub, SubAdmin)
class SubAdditionAdmin(admin.ModelAdmin):
    list_display = ['title', "price"]
    list_filter = ["price"]
    list_editable = ["price"]
admin.site.register(models.SubAddition, SubAdditionAdmin)

class PastaAdmin(admin.ModelAdmin):
    list_display = ['title', "price"]
    list_filter = ["price"]
    list_editable = ["price"]
admin.site.register(models.Pasta, PastaAdmin)
class SaladAdmin(admin.ModelAdmin):
    list_display = ['title', "price"]
    list_filter = ["price"]
    list_editable = ["price"]
admin.site.register(models.Salad, SaladAdmin)
class DinnerPlatterAdmin(admin.ModelAdmin):
    list_display = ['title', "size", "price"]
    list_filter = ["size", "price"]
    list_editable = ["price"]
admin.site.register(models.DinnerPlatter, DinnerPlatterAdmin)
