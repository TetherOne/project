from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cart.views import CartViewSet

app_name = "cart"


routers = DefaultRouter()


routers.register(
    'carts',
    CartViewSet,
)


urlpatterns = [
    path("", include(routers.urls)),
]