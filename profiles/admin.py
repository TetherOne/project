from profiles.models import ClientProfile

from django.contrib import admin


@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "surname",
        "father_name",
    )
