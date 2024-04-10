from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers

from django.contrib.auth import get_user_model

from profiles.models import ClientProfile
from profiles.serializers import ClientSerializer



class CurrentUserSerializer(serializers.ModelSerializer):

    user_profile = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "email",
            "user_profile",
        ]

    def get_user_profile(self, obj):
        """
        Getting a profile for the current
        authenticated user
        """

        try:
            client_profile = obj.client_profile
            serializer = ClientSerializer(client_profile)
        except ClientProfile.DoesNotExist:
            return None
        return serializer.data

    def to_representation(self, instance):
        if isinstance(instance, AnonymousUser):
            return {
                "id": None,
                "username": None,
                "email": None,
                "date_joined": None,
                "user_profile": None,
            }
        return super().to_representation(instance)