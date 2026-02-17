from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    product_name = models.CharField(max_length=200)          # e.g., "4x1.5 mm² Cable"
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    price_q1 = models.DecimalField(max_digits=10, decimal_places=2)
    price_q2 = models.DecimalField(max_digits=10, decimal_places=2)
    price_q3 = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('product_name', 'category', 'company')

    def __str__(self):
        return f"{self.product_name} - {self.category} - {self.company}"
    


class Quotation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.TextField()   # store JSON string; if using PostgreSQL you can use JSONField

    def __str__(self):
        return f"Quotation #{self.id} by {self.user.username}"