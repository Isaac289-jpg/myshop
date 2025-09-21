from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # 👈 link product to category
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=100)  # Customer name
    email = models.EmailField()              # Customer email
    product = models.CharField(max_length=200)  # Product name (e.g., Shoes, Watch, Cloth)
    quantity = models.PositiveIntegerField(default=1)
    address = models.TextField()             # Delivery address
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product}"

