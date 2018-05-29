from django.db import models


# Create your models here.
# BASE CLASSES
class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.title}"


class SizedMenutIem(MenuItem):
    SIZE_CHOICES = ( ("small", "Small"), ("large", "Large") )
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.title} ({self.size})"


# MODELS
class Pizza(SizedMenutIem):
    KIND_CHOICES = ( ("regular", "Regular"), ("sicilian", "Sicilian") )
    kind = models.CharField(max_length=10, choices=KIND_CHOICES)
    toppings_number = models.IntegerField()

    def __str__(self):
        return f"{self.title} {self.kind} pizza ({self.size}) with {self.toppings_number} toppings"


class PizzaTopping(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"


class SubAddition(MenuItem):
    pass

class Sub(SizedMenutIem):
    pass

class Pasta(MenuItem):
    pass

class Salad(MenuItem):
    pass

class DinnerPlatter(SizedMenutIem):
    pass
