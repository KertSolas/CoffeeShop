from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Product, CoffeeName
# Create your views here.

class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    success_url = reverse_lazy('coffeeNames')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coffee_names'] = CoffeeName.objects.all()  # Pass CoffeeName objects to the context
        return context

def buy():
    return   