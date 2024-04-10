from django.db import models


class DishInfo(models.Model):

    weight = models.FloatField(blank=True, null=True, default=0)
    proteins = models.FloatField(blank=True, null=True, default=0)
    carbohydrates = models.FloatField(blank=True, null=True, default=0)
    fats = models.FloatField(blank=True, null=True, default=0)
    kilocalories_per_100_grams = models.FloatField(
        blank=True,
        null=True,
        default=0,
    )
    dish = models.OneToOneField(
        'Dish',
        on_delete=models.CASCADE,
    )


class Dish(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    preview = models.ImageField(
        null=True,
        upload_to="dishes-preview/",
        blank=True,
    )

    def save(self, *args, **kwargs):
        """
        Создание DishInfo после создания блюда
        """
        super(Dish, self).save(*args, **kwargs)
        if not hasattr(self, 'dishinfo'):
            DishInfo.objects.create(dish=self)


    def __str__(self):
        return f'{self.name} - {self.price}'


class DishImages(models.Model):
    pass