from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from profiles.models import AdminProfile, ClientProfile
from profiles.serializers import ClientSerializer


class AdminViewSet(ModelViewSet):

    serializer_class = ClientSerializer
    queryset = AdminProfile.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user"]


class ClientViewSet(ModelViewSet):

    serializer_class = ClientSerializer
    queryset = ClientProfile.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user"]


