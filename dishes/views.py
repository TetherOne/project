from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from dishes.models import Dish, DishInfo, DishImages, Category
from dishes.serializers import DishSerializer, DishInfoSerializer, DishImagesSerializer, DishCategorySerializer


class DishViewSet(ModelViewSet):

    serializer_class = DishSerializer
    queryset = Dish.objects.all()
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
        "dish"
    ]


class DishCategoryViewSet(ModelViewSet):

    serializer_class = DishCategorySerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "category",
    ]


class DishImagesViewSet(ModelViewSet):

    serializer_class = DishImagesSerializer
    queryset = DishImages.objects.all()