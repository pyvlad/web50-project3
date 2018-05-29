from django.http import HttpResponse
from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    cats = models.Category.objects.all()
    data = []
    for cat in cats:
        data += [(cat, models.Product.objects.filter(category=cat))]
    return render(request, "orders/index.html", {"data": data})
