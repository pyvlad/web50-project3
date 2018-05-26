from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Pizza)
admin.site.register(models.PizzaTopping)
admin.site.register(models.Sub)
admin.site.register(models.SubAddition)
admin.site.register(models.Pasta)
admin.site.register(models.Salad)
admin.site.register(models.DinnerPlatter)
