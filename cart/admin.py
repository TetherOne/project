from django.contrib import admin

from cart.models import Cart, CartDish
from profiles.models import ClientProfile

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ('id', 'profile',)
    list_display_links = ('id', 'profile',)


@admin.register(CartDish)
class CartDishAdmin(admin.ModelAdmin):

    list_display = ('id', 'cart', 'dish', 'quantity',)
    list_display_links = ('id', 'cart', 'dish', 'quantity',)
    # search_fields = ()
    list_filter = ('cart', 'dish', 'quantity',)
    ordering = ('id',)
