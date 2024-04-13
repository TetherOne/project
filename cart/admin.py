from cart.models import CartDish
from cart.models import Cart

from django.contrib import admin


class CartDishInline(admin.TabularInline):
    model = CartDish


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    inlines = [
        CartDishInline,
    ]
    list_display = (
        "id",
        "profile",
    )
    search_fields = (
        "profile__name",
        "profile__surname",
        "profile__father_name",
    )
    list_display_links = (
        "id",
        "profile",
    )


@admin.register(CartDish)
class CartDishAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "cart",
        "dish",
        "quantity",
    )
    list_display_links = (
        "id",
        "cart",
        "dish",
        "quantity",
    )
    search_fields = (
        "cart__profile__name",
        "cart__profile__surname",
        "cart__profile__father_name",
    )
    list_filter = (
        "cart",
        "dish",
        "quantity",
    )
    ordering = ("id",)
