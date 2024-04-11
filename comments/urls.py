from rest_framework.routers import DefaultRouter

from comments.views import CommentViewSet

from django.urls import include
from django.urls import path


app_name = "comments"


routers = DefaultRouter()


routers.register(
    "comments",
    CommentViewSet,
)


urlpatterns = [
    path("", include(routers.urls)),
]
