from django_filters.rest_framework import DjangoFilterBackend

from cart.serializers import CartDishSerializer
from cart.serializers import CartSerializer

from rest_framework import viewsets

from cart.models import CartDish
from cart.models import Cart


class CartViewSet(viewsets.ModelViewSet):

    queryset = Cart.objects.prefetch_related(
        "profile",
    ).all()
    serializer_class = CartSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "profile",
    ]


class CartDishViewSet(viewsets.ModelViewSet):

    queryset = CartDish.objects.all()
    serializer_class = CartDishSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "cart_id",
        "dish_id",
    ]
