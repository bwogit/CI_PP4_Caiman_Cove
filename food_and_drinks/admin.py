from django.contrib import admin
from .models import FoodMenuItem, DrinkMenuItem
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(FoodMenuItem)
class FoodMenuAdmin(SummernoteModelAdmin):
    list_filter = ('available', 'food_type')
    summernote_fields = ('food_description')


@admin.register(DrinkMenuItem)
class DrinkMenuAdmin(SummernoteModelAdmin):
    list_filter = ('available', 'drink_type')
    summernote_fields = ('drink_description')    