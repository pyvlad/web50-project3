from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import models


# Create your views here.
def index(request):
    cats = models.Category.objects.all()
    data = []
    for cat in cats:
        data += [(cat, models.Product.objects.filter(category=cat))]
    return render(request, "orders/index.html", {"data": data})


@login_required
def cart(request):
    try:
        cart = models.Cart.objects.get(user=request.user)
    except models.Cart.DoesNotExist:
        cart = models.Cart(user=request.user)
        cart.save()
    return render(request, "orders/cart.html", {"cart": cart})


@login_required
def add_to_cart(request):
    try:
        product_id = int(request.POST["product_id"])
        product = models.Product.objects.get(id=product_id)
    except (KeyError, ValueError, models.Product.DoesNotExist):
        return HttpResponseBadRequest()

    try:
        cart = models.Cart.objects.get(user=request.user)
    except models.Cart.DoesNotExist:
        cart = models.Cart(user=request.user)
        cart.save()

    cart.products.add(product)
    return HttpResponseRedirect(reverse("cart"))
