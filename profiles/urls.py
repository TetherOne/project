from rest_framework.routers import DefaultRouter

from profiles.views import ClientViewSet
from profiles.views import UserViewSet

from django.urls import include
from django.urls import path


app_name = "profiles"


routers = DefaultRouter()


routers.register(
    "users",
    UserViewSet,
    basename="users",
)
routers.register(
    "clients",
    ClientViewSet,
)


urlpatterns = [
    path("", include(routers.urls)),
]
