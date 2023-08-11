from django.contrib import admin
from .models import FoodMenuItem, DrinkMenuItem
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(FoodMenuItem())
class FoodMenuAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')


@admin.register(DrinkMenuItem())
class DrinkMenuAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')    