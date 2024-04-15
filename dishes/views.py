from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser

from dishes.serializers import DishCategorySerializer
from dishes.serializers import DishImagesSerializer
from dishes.serializers import DishInfoSerializer
from dishes.serializers import DishSerializer

from rest_framework.viewsets import ModelViewSet

from dishes.models import DishCategory
from dishes.models import DishImages
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

    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "name",
    ]
    ordering_fields = [
        "name",
        "price",
    ]


class DishInfoViewSet(PermissionViewSet, ModelViewSet):

    queryset = DishInfo.objects.all()
    serializer_class = DishInfoSerializer
    ordering_fields = [
        "weight",
        "proteins",
        "carbohydrates",
        "fats",
        "kilocalories_per_100_grams",
        "dish",
    ]


class DishCategoryViewSet(PermissionViewSet, ModelViewSet):

    queryset = DishCategory.objects.all()
    serializer_class = DishCategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "name",
    ]


class DishImagesViewSet(PermissionViewSet, ModelViewSet):

    queryset = DishImages.objects.all()
    serializer_class = DishImagesSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = [
        "dish",
    ]
