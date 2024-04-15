from rest_framework import serializers

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(
        source="author.name",
    )
    author_surname = serializers.ReadOnlyField(
        source="author.surname",
    )
    author_father_name = serializers.ReadOnlyField(
        source="author.father_name",
    )

    class Meta:
        model = Comment
        fields = "__all__"
