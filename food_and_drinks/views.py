from django.shortcuts import render
from django.views.generic import ListView
from .models import FoodMenuItem, DrinkMenuItem

def food_menu(request):
    food_list = FoodMenuItem.objects.all()
    return render(request, 'food_menu.html', {'food_list': food_list})


def drink_menu(request):
    drink_list = DrinkMenuItem.objects.all()
    return render(request, 'drink_menu.html', {'drink_list': drink_list})


class FoodMenuListView(ListView):
    """
    Class-based view to display the food menu items.
    """
    model = FoodMenuItem
    template_name = 'food_menu.html'
    context_object_name = 'food_items'
    queryset = FoodMenuItem.objects.filter(food_available=True).order_by('food_item_type')
       

class DrinkMenuListView(ListView):
    """
    Class-based view to display the drink menu items.
    """
    model = DrinkMenuItem
    template_name = 'drink_menu.html'
    context_object_name = 'drink_items'
    queryset = DrinkMenuItem.objects.filter(drink_available=True).order_by('drink_item_type')
