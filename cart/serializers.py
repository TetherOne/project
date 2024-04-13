from rest_framework import serializers

from cart.models import Cart, CartDish


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDish
        fields = "__all__"