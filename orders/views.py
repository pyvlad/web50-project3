from django.http import HttpResponse
from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    return render(request, "orders/index.html", {
        "pizzas": models.Pizza.objects.all(),
        "pizzatoppings": models.PizzaTopping.objects.all(),
        "subs": models.Sub.objects.all(),
        "subadditions": models.SubAddition.objects.all(),
        "pastas": models.Pasta.objects.all(),
        "salads": models.Salad.objects.all(),
        "dinnerplatters": models.DinnerPlatter.objects.all(),
        }
    )
