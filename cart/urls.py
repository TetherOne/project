from rest_framework.routers import DefaultRouter

from cart.views import CartViewSet

from django.urls import include
from django.urls import path


app_name = "cart"


routers = DefaultRouter()


routers.register(
    "carts",
    CartViewSet,
)


urlpatterns = [
    path("", include(routers.urls)),
]
