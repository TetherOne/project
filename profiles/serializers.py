from rest_framework import serializers

from profiles.models import ClientProfile, AdminProfile


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = "__all__"


