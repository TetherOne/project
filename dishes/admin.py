from dishes.models import DishCategory
from dishes.models import Dish

from django.contrib import admin


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "description",
        "get_category_name",
        "price",
    )
    list_display_links = ("name",)
    search_fields = (
        "name",
        "description",
        "category__name",
        "price",
    )
    list_filter = (
        "category",
        "price",
    )
    ordering = (
        "id",
        "name",
        "price",
        "category",
    )

    def get_category_name(self, obj):
        return obj.category.name

    get_category_name.short_description = "Category"


@admin.register(DishCategory)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "dish_count",
    )
    list_display_links = (
        "id",
        "name",
    )
    search_fields = (
        "id",
        "name",
    )
    list_filter = (
        "name",
        "dish_count",
    )
    ordering = ("id",)
