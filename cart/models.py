from profiles.models import ClientProfile

from dishes.models import Dish

from django.db import models


class Cart(models.Model):

    count = models.PositiveIntegerField(default=1)
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
    )
    profile = models.ForeignKey(
        ClientProfile,
        on_delete=models.CASCADE,
    )
