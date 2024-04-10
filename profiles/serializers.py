from rest_framework import serializers

from authentication.models import CustomUser
from profiles.models import ClientProfile


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
        is_teacher = validated_data.pop("is_teacher", False)
        user = CustomUser.objects.create_user(**validated_data)

        ClientProfile.objects.create(user=user)

        return user

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #
    #     if hasattr(instance, "teacher_profile"):
    #         data["is_teacher"] = True
    #     else:
    #         data["is_teacher"] = False
    #     return data