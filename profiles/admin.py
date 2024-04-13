from profiles.models import ClientProfile

from django.contrib import admin


@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "surname",
        "father_name",
        "created_at",
    )
    list_display_links = (
        "id",
        "name",
        "surname",
        "father_name",
    )
    search_fields = (
        "id",
        "name",
        "surname",
        "father_name",
    )
    list_filter = (
        "name",
        "surname",
        "father_name",
        "created_at",
    )
    ordering = (
        "id",
        "name",
        "surname",
        "father_name",
        "created_at",
    )
