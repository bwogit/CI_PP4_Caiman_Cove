from django.views.generic import ListView
from .models import FoodMenuItem, DrinkMenuItem

class FoodMenuListView(ListView):
    """
    Class-based view to display the food menu items.
    """
    model = FoodMenuItem
    template_name = 'food_menu.html'
    context_object_name = 'food_items'
    queryset = FoodMenuItem.objects.filter(food_available=True)

class DrinkMenuListView(ListView):
    """
    Class-based view to display the drink menu items.
    """
    model = DrinkMenuItem
    template_name = 'drink_menu.html'
    context_object_name = 'drink_items'
    queryset = DrinkMenuItem.objects.filter(drink_available=True)
