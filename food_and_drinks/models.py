from django.db import models

# Create your models here.
FOOD_ITEM_TYPE = ((0, 'Starters'), (1, 'Mains'), (2, 'Desserts'), (3, 'AddItem'))
DRINK_ITEM_TYPE = ((0, 'Soft'), (1, 'Wine'), (2, 'Beers'), (3, 'AddItem'))

class FoodMenuItem(models.Model):


class DrinkMenuItem(models.Model):    