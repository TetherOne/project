from rest_framework.routers import DefaultRouter

from favorites.views import FavoritesViewSet

from django.urls import include
from django.urls import path


app_name = "favorites"


routers = DefaultRouter()


routers.register(
    "favorites",
    FavoritesViewSet,
)


urlpatterns = [
    path("", include(routers.urls)),
]
