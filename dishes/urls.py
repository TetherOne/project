from rest_framework.routers import DefaultRouter

from dishes.views import DishCategoryViewSet
from dishes.views import DishImagesViewSet
from dishes.views import DishInfoViewSet
from dishes.views import DishViewSet

from django.urls import include
from django.urls import path


app_name = "dishes"


routers = DefaultRouter()


routers.register(
    "dishes",
    DishViewSet,
)
routers.register(
    "dish_info",
    DishInfoViewSet,
)
routers.register(
    "dish_categories",
    DishCategoryViewSet,
)
routers.register(
    "dish_images",
    DishImagesViewSet,
)


urlpatterns = [
    path("", include(routers.urls)),
]
