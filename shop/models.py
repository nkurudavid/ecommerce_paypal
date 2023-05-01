from django.db import models
from django.contrib.auth import get_user_model

User =get_user_model()

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, verbose_name="Product Category", related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="PRoduct name",)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, help_text="Price of the product (in dollars or dollars if  no price is specified).")
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, help_text="product image")
    def __str__(self):
        return self.name


class Order(models.Model):
    orderCode = models.CharField(max_length=255, verbose_name="Order Number", unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    is_paid = models.BooleanField(default=False , verbose_name="Payment Status",)
    dateCreated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.orderCode


