from django.contrib import admin
from .models import FoodMenuItem, DrinkMenuItem

# Register your models here.
admin.site.register(FoodMenuItem)
admin.site.register(DrinkMenuItem)
