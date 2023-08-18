from django.urls import path
from .views import FoodMenuListView, DrinkMenuListView

urlpatterns = [
    path('food_menu/', FoodMenuListView.as_view(), name='food_menu'),
    path('drink_menu/', DrinkMenuListView.as_view(), name='drink_menu'),
]
