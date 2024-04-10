from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from authentication.models import CustomUser
from profiles.models import ClientProfile
from profiles.serializers import ClientSerializer, UserRegistrationSerializer


class ClientViewSet(ModelViewSet):

    serializer_class = ClientSerializer
    queryset = ClientProfile.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user"]


class UserViewSet(ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        serializer.save()
