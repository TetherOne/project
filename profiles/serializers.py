from authentication.models import CustomUser
from profiles.models import ClientProfile

from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = "__all__"


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser
        fields = (
            "id",
            "email",
            "username",
            "password",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        For creating a user profile
        """
        user = CustomUser.objects.create_user(**validated_data)
        ClientProfile.objects.create(user=user)

        return user
