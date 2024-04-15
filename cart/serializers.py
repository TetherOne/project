from rest_framework import serializers

from cart.models import CartDish
from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField(
        source="profile.name",
    )
    surname = serializers.ReadOnlyField(
        source="profile.surname",
    )
    father_name = serializers.ReadOnlyField(
        source="profile.father_name",
    )

    class Meta:
        model = Cart
        fields = "__all__"


class CartDishSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartDish
        fields = "__all__"
