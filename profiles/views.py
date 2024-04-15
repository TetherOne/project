from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAdminUser

from profiles.serializers import UserRegistrationSerializer
from profiles.serializers import ClientSerializer

from rest_framework.viewsets import ModelViewSet

from authentication.models import CustomUser

from profiles.models import ClientProfile


class PermissionViewSet(ModelViewSet):
    permission_classes_by_action = {
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }

    def get_permissions(self) -> list:
        return [
            permission()
            for permission in self.permission_classes_by_action.get(
                self.action,
                [],
            )
        ]


class ClientViewSet(ModelViewSet):

    serializer_class = ClientSerializer
    queryset = ClientProfile.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "user",
    ]


class UserViewSet(ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        serializer.save()
