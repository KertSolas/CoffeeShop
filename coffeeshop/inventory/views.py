from django.shortcuts import render
from django.http import *
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import CoffeeName
# Create your views here.

class coffeeList(ListView): 
    model = CoffeeName

class AddCoffee(CreateView): 
    model = CoffeeName
    template_name = "inventory/addCoffee.html"
    fields = '__all__'
    success_url = reverse_lazy('coffeeNames')

class DeleteCoffee(DeleteView):
    model = CoffeeName
    template_name = "inventory/deleteCoffee.html"
    context_object_name = "coffee"
    success_url = reverse_lazy('coffeeNames')