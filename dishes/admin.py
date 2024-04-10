from django.contrib import admin

from dishes.models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):

    list_display = ("name", "description", "price")
    list_display_links = ("name",)
    search_fields = ("name",)
    list_filter = ("name", "price",)
    ordering = ("id",)