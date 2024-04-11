from django_filters.rest_framework import DjangoFilterBackend

from cart.serializers import CartSerializer

from rest_framework import viewsets

from cart.models import Cart


class CartViewSet(viewsets.ModelViewSet):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "dish",
        "profile",
    ]
