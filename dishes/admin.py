from dishes.models import Category
from dishes.models import Dish

from django.contrib import admin


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "description",
        "price",
    )
    list_display_links = ("name",)
    search_fields = ("name",)
    list_filter = (
        "name",
        "price",
    )
    ordering = ("id",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("id",)
