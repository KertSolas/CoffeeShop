from django.db import models
from inventory.models import CoffeeName

# Create your models here.

class Product(models.Model): 
    productName = models.ForeignKey(CoffeeName, on_delete=models.CASCADE)
    stock = models.IntegerField(null=True, blank=True)
    isAvailable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productName.title

