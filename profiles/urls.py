from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles.views import ClientViewSet, UserViewSet

app_name = "profiles"


routers = DefaultRouter()


routers.register(
    "users",
    UserViewSet,
    basename="users",
)
routers.register(
    'clients',
    ClientViewSet,
)


urlpatterns = [
    path("", include(routers.urls)),
]