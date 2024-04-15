from django_filters.rest_framework import DjangoFilterBackend

from comments.serializers import CommentSerializer

from rest_framework.viewsets import ModelViewSet

from comments.models import Comment


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.prefetch_related(
        "dish",
        "author",
    ).all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "dish",
        "author",
    ]
