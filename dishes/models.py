from django.db import models

import re


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
        "Dish",
        on_delete=models.CASCADE,
    )


class Dish(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    category = models.ForeignKey(
        "DishCategory",
        on_delete=models.CASCADE,
        related_name="dishes",
    )
    preview = models.ImageField(
        null=True,
        upload_to="dishes-preview/",
        blank=True,
    )

    def save(self, *args, **kwargs):
        """
        Creating DishInfo (information about a
        dish: kcal, proteins, carbohydrates,
        etc.) after creating a dish
        """
        super(Dish, self).save(*args, **kwargs)
        if not hasattr(self, "dishinfo"):
            DishInfo.objects.create(dish=self)
        self.category.update_dish_count()

    def delete(self, *args, **kwargs):
        category = self.category
        super(Dish, self).delete(*args, **kwargs)
        category.update_dish_count()

    def update(self):
        self.category.update_dish_count()

    def __str__(self):
        return f"{self.name} - {self.price}"


def dish_images_file_path(
    instance: "Dish",
    filename,
) -> str:
    """
    For saving additional dish images
    """
    valid_filename = re.sub(
        r"[\\/*?:\"<>|]",
        "_",
        filename,
    )
    return f"dishes/{instance.dish.name}/images/{valid_filename}"


class DishImages(models.Model):

    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        related_name="dish_images",
    )
    dish_images = models.ImageField(
        null=True,
        upload_to=dish_images_file_path,
        blank=True,
    )


class DishCategory(models.Model):

    name = models.CharField(max_length=255)
    dish_count = models.IntegerField(default=0)

    def update_dish_count(self):
        self.dish_count = self.dishes.count()
        self.save()

    def __str__(self):
        return f"{self.name}"
