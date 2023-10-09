from django.db import models

# Create your models here.

class CoffeeName(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class CakeName(models.Model): 
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    