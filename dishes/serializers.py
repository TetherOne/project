from rest_framework import serializers

from dishes.models import Dish, DishInfo, Category, DishImages


class DishInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishInfo
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class DishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DishImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishImages
        fields = '__all__'