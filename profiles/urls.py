from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles.views import AdminViewSet, ClientViewSet

app_name = "profiles"


routers = DefaultRouter()


routers.register(
    'admins',
    AdminViewSet,
)
routers.register(
    'clients',
    ClientViewSet,
)


urlpatterns = [
    path("", include(routers.urls)),
]