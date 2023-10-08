from django.urls import path
from django.contrib import admin
from .views import coffeeList, AddCoffee, DeleteCoffee

urlpatterns = [
    path("", coffeeList.as_view(), name="coffeeNames"),
    path("addCoffee/", AddCoffee.as_view(), name="addCoffee"),
    path("deleteCoffee/<int:pk>/", DeleteCoffee.as_view(), name="deleteCoffee"),
    path('admin/', admin.site.urls,)
]