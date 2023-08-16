from django.urls import path
from .views import FoodMenuListView, DrinkMenuListView

urlpatterns = [
    path('food-menu/', FoodMenuListView.as_view(), name='food_menu'),
    path('drink-menu/', DrinkMenuListView.as_view(), name='drink_menu'),
]