from django.urls import path
from django.contrib import admin
from shop.views import ProductList

urlpatterns = [
    path("", ProductList.as_view(), name="products_list"),
]