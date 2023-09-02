# Imports
# 3rd Party:
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Internals
from .models import FoodMenuItem, DrinkMenuItem


@admin.register(FoodMenuItem)
class FoodMenuAdmin(SummernoteModelAdmin):
    list_display = ('food_item_name', 'food_item_type',
                    'food_price', 'food_available')
    search_fields = ('food_item_name', 'food_description')
    list_filter = ('food_available', 'food_item_type')
    summernote_fields = ('food_description')


@admin.register(DrinkMenuItem)
class DrinkMenuAdmin(SummernoteModelAdmin):
    list_display = ('drink_item_name', 'drink_item_type',
                    'drink_price', 'drink_available')
    search_fields = ('drink_item_name', 'drink_description')
    list_filter = ('drink_available', 'drink_item_type')
    summernote_fields = ('drink_description')
