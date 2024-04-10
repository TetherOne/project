from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import CurrentUserSerializer


class CurrentUserView(APIView):
    def get(self, request):
        serializer = CurrentUserSerializer(request.user)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
