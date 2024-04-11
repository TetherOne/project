from django.db import models

from dishes.models import Dish


class Cart(models.Model):

    count = models.PositiveIntegerField(default=1)
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
    )
    profile = models.ForeignKey(
        'profiles.ClientProfile',
        on_delete=models.CASCADE,
    )


