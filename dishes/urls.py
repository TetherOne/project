from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dishes.views import DishViewSet, DishInfoViewSet

app_name = "dishes"


routers = DefaultRouter()


routers.register(
    'dishes',
    DishViewSet,
)
routers.register(
    'dishes_info',
    DishInfoViewSet,
)

urlpatterns = [
    path("", include(routers.urls)),
]