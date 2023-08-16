from django.shortcuts import render
from django.views.generic import ListView
from .models import FoodMenuItem, DrinkMenuItem

def food_menu(request):
    return render(request, 'food_menu.html')


def drink_menu(request):
    return render(request, 'drink_menu.html')


class FoodMenuListView(ListView):
    """
    Class-based view to display the food menu items.
    """
    model = FoodMenuItem
    template_name = 'food_menu.html'
    context_object_name = 'food_items'
    queryset = FoodMenuItem.objects.filter(food_available=True).order_by('-food_item_type')

class DrinkMenuListView(ListView):
    """
    Class-based view to display the drink menu items.
    """
    model = DrinkMenuItem
    template_name = 'drink_menu.html'
    context_object_name = 'drink_items'
    queryset = DrinkMenuItem.objects.filter(drink_available=True)
