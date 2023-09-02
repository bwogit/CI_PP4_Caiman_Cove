# Imports
# 3rd party:
from django.urls import path
# Internals
from .views import FoodMenuListView, DrinkMenuListView

urlpatterns = [
    path('food_menu/', FoodMenuListView.as_view(), name='food_menu'),
    path('drink_menu/', DrinkMenuListView.as_view(), name='drink_menu'),
]
