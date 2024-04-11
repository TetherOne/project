from django_filters.rest_framework import DjangoFilterBackend

from favorites.serializers import FavoritesSerializer

from rest_framework.viewsets import ModelViewSet

from favorites.models import Favorites


class FavoritesViewSet(ModelViewSet):

    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "dish",
        "profile",
    ]
