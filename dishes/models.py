from django.db import models


class DishInfo(models.Model):

    weight = models.FloatField()
    proteins = models.FloatField()
    carbohydrates = models.FloatField()
    fats = models.FloatField()
    kilocalories_per_100_grams = models.FloatField()


class Dish(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    nutritional_value = models.OneToOneField(
        DishInfo,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name} - {self.price}'