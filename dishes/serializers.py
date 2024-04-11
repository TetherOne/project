from rest_framework import serializers

from dishes.models import DishImages
from dishes.models import DishInfo
from dishes.models import Category
from dishes.models import Dish


class DishInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishInfo
        fields = "__all__"


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"


class DishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class DishImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishImages
        fields = "__all__"
