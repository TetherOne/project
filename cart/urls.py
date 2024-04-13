from rest_framework.routers import DefaultRouter

from cart.views import CartViewSet, CartDishViewSet

from django.urls import include
from django.urls import path


app_name = "cart"


routers = DefaultRouter()


routers.register(
    "carts",
    CartViewSet,
)
routers.register(
    "cart-dishes",
    CartDishViewSet,
)


urlpatterns = [
    path("", include(routers.urls)),
]
