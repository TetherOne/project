from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dishes.views import DishViewSet

app_name = "dishes"


routers = DefaultRouter()


routers.register(
    'dishes',
    DishViewSet,
)


urlpatterns = [
    path("", include(routers.urls)),
]