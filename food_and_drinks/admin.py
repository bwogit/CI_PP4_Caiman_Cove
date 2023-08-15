from django.contrib import admin
from .models import FoodMenuItem, DrinkMenuItem
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(FoodMenuItem)
class FoodMenuAdmin(SummernoteModelAdmin):
    list_display = ('food_name', 'food_type', 'price', 'available')
    search_fields = ('food_name', 'description')
    list_filter = ('available', 'food_type')
    summernote_fields = ('food_description')


@admin.register(DrinkMenuItem)
class DrinkMenuAdmin(SummernoteModelAdmin):
    list_display = ('drink_name', 'drink_type', 'price', 'available')
    search_fields = ('drink_name', 'description')
    list_filter = ('available', 'drink_type')
    summernote_fields = ('drink_description')    