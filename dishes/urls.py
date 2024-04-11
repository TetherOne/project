from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dishes.views import DishViewSet, DishInfoViewSet, DishCategoryViewSet, DishImagesViewSet

app_name = "dishes"


routers = DefaultRouter()


routers.register(
    'dishes',
    DishViewSet,
)
routers.register(
    'dish_info',
    DishInfoViewSet,
)
routers.register(
    'dish_categories',
    DishCategoryViewSet,
)
routers.register(
    'dish_images',
    DishImagesViewSet,
)

urlpatterns = [
    path("", include(routers.urls)),
]