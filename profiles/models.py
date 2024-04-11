from authentication.models import CustomUser

from django.db import models


class ClientProfile(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="client_profile",
    )

    def __str__(self):
        return f"{self.name} {self.surname} {self.father_name}"
