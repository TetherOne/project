from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from dishes.models import Dish, DishInfo
from dishes.serializers import DishSerializer, DishInfoSerializer


class DishViewSet(ModelViewSet):

    serializer_class = DishSerializer
    queryset = Dish.objects.select_related('dishinfo').all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "name",
    ]
    ordering_fields = [
        "name",
        "price",
    ]


class DishInfoViewSet(ModelViewSet):

    serializer_class = DishInfoSerializer
    queryset = DishInfo.objects.all()
    ordering_fields = [
        "weight",
        "proteins",
        "carbohydrates",
        "fats",
        "kilocalories_per_100_grams",
    ]


