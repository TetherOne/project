from rest_framework import serializers

from dishes.models import Dish, DishInfo


class DishInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishInfo
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):

    dishinfo = DishInfoSerializer()

    class Meta:
        model = Dish
        fields = '__all__'

