from django.db import models

# Create your models here.
FOOD_ITEM_TYPE = ((0, 'Starters'), (1, 'Mains'), (2, 'Desserts'), (3, 'AddItem'))
DRINK_ITEM_TYPE = ((0, 'Soft'), (1, 'Wine'), (2, 'Beers'), (3, 'AddItem'))

class FoodMenuItem(models.Model):
    """
    Food item model
    """
    food_item_id = models.AutoField(primary_key=True)
    food_item_name = models.CharField(max_length=50, unique=True)
    food_description = models.CharField(max_length=200, unique=True)
    food_price = models.FloatField()
    food_item_type = models.IntegerField(choices=FOOD_ITEM_TYPE, default=3)
    food_available = models.BooleanField(default=False)

    class Meta:
        ordering = ['-food_available']

    def __str__(self):
        return self.food_item_name



class DrinkMenuItem(models.Model):
    """
    Drink item model
    """
    drink_item_id = models.AutoField(primary_key=True)
    drink_item_name = models.CharField(max_length=50, unique=True)
    drink_description = models.CharField(max_length=200, unique=True)
    drink_price = models.FloatField()
    drink_item_type = models.IntegerField(choices=DRINK_ITEM_TYPE, default=3)
    drink_available = models.BooleanField(default=False)

    class Meta:
        ordering = ['-drink_available']

    def __str__(self):
        return self.drink_item_name

    