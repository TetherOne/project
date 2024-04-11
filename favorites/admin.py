from django.contrib import admin

from favorites.models import Favorites


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):

    list_display = (
        "profile",
        "dish",
    )
    list_display_links = ("profile",)
    search_fields = ("profile",)
    list_filter = ("profile",)
    ordering = ("id",)
