from django.urls import path, include
from rest_framework.routers import DefaultRouter

from comments.views import CommentViewSet

app_name = "comments"


routers = DefaultRouter()


routers.register(
    'comments',
    CommentViewSet,
)


urlpatterns = [
    path("", include(routers.urls)),
]