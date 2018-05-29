from django.db import models
from django.conf import settings


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name}"


class ProductSize(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="products")
    size = models.ForeignKey("ProductSize", on_delete=models.CASCADE, related_name="products", null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        if self.size:
            size = "[{}]".format(self.size.name[0])
        else:
            size = ""
        return f"{self.name} {size}"


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True, related_name="carts")

    def __str__(self):
        return f"{self.user.username}"

    def total_sum(self):
        return sum(filter(None, [product.price for product in self.products.all()]))
