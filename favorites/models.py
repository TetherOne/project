from django.db import models


class Favorites(models.Model):

    profile = models.ForeignKey(
        "profiles.ClientProfile",
        on_delete=models.CASCADE,
    )
    dish = models.ForeignKey(
        "dishes.Dish",
        on_delete=models.CASCADE,
    )
