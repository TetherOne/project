from favorites.models import Favorites

from django.contrib import admin


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "profile",
        "dish",
    )
    list_display_links = (
        "profile",
        "dish",
    )
    search_fields = (
        "profile__name",
        "profile__surname",
        "profile__father_name",
        "dish__name",
    )
    list_filter = (
        "profile__name",
        "profile__surname",
        "profile__father_name",
        "dish",
    )
    ordering = ("id",)
