from django.db import models


# Create your models here.
class Pizza(models.Model):
    SIZE_CHOICES = ( ("small", "Small"), ("large", "Large") )
    KIND_CHOICES = ( ("regular", "Regular"), ("sicilian", "Sicilian") )

    title = models.CharField(max_length=100)
    kind = models.CharField(max_length=10, choices=KIND_CHOICES)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    toppings_number = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.title} {self.kind} pizza ({self.size}) with {self.toppings_number} toppings"


class PizzaTopping(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"


class SubAddition(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.title}"


class Sub(models.Model):
    SIZE_CHOICES = ( ("small", "Small"), ("large", "Large") )

    title = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    price = models.FloatField()

    def __str__(self):
        return f"{self.title} ({self.size})"



class Pasta(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.title}"


class Salad(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.title}"


class DinnerPlatter(models.Model):
    SIZE_CHOICES = ( ("small", "Small"), ("large", "Large") )

    title = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    price = models.FloatField()

    def __str__(self):
        return f"{self.title} ({self.size})"
