from profiles.models import ClientProfile

from dishes.models import Dish

from django.db import models


class Cart(models.Model):

    profile = models.OneToOneField(
        ClientProfile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.profile}"


class CartDish(models.Model):

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="cart_dishes",
    )
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(default=1)
