from django.db import models


class Comment(models.Model):

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    dish = models.ForeignKey(
        "dishes.Dish",
        on_delete=models.CASCADE,
    )
    author = models.OneToOneField(
        "profiles.ClientProfile",
        on_delete=models.CASCADE,
    )
