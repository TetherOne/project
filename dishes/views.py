from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from dishes.models import Dish
from dishes.serializers import DishSerializer


class DishViewSet(ModelViewSet):
    serializer_class = DishSerializer
    queryset = Dish.objects
