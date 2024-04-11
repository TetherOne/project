from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser

from dishes.serializers import DishCategorySerializer
from dishes.serializers import DishImagesSerializer
from dishes.serializers import DishInfoSerializer
from dishes.serializers import DishSerializer

from rest_framework.viewsets import ModelViewSet

from dishes.models import DishImages
from dishes.models import Category
from dishes.models import DishInfo
from dishes.models import Dish


class PermissionViewSet(ModelViewSet):
    permission_classes_by_action = {
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }

    def get_permissions(self) -> list:
        return [
            permission()
            for permission in self.permission_classes_by_action.get(
                self.action,
                [],
            )
        ]


class DishViewSet(PermissionViewSet, ModelViewSet):

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


class DishInfoViewSet(PermissionViewSet, ModelViewSet):

    serializer_class = DishInfoSerializer
    queryset = DishInfo.objects.all()
    ordering_fields = [
        "weight",
        "proteins",
        "carbohydrates",
        "fats",
        "kilocalories_per_100_grams",
        "dish",
    ]


class DishCategoryViewSet(PermissionViewSet, ModelViewSet):

    serializer_class = DishCategorySerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "category",
    ]


class DishImagesViewSet(PermissionViewSet, ModelViewSet):

    serializer_class = DishImagesSerializer
    queryset = DishImages.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = [
        "dish",
    ]
