from django.urls import path
from django.contrib import admin
from .views import coffeeList, AddCoffee, DeleteCoffee, UpdateCoffee

urlpatterns = [
    path("", coffeeList.as_view(), name="coffeeNames"),
    path("addCoffee/", AddCoffee.as_view(), name="addCoffee"),
    path("deleteCoffee/<int:pk>/", DeleteCoffee.as_view(), name="deleteCoffee"),
    path("updateCoffee/<int:pk>/", UpdateCoffee.as_view(), name="updateCoffee"),
    path('admin/', admin.site.urls,)
]