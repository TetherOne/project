from comments.models import Comment

from django.contrib import admin


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "short_text",
        "dish",
        "author",
        "created_at",
    )
    search_fields = (
        "id",
        "text",
        "dish__name",
        "author__name",
        "author__surname",
        "author__father_name",
    )
    list_display_links = (
        "id",
        "short_text",
        "dish",
        "author",
    )
    list_filter = (
        "dish",
        "author__name",
        "author__surname",
        "author__father_name",
    )
    ordering = ("id",)

    def short_text(self, obj):
        if len(obj.text) > 40:
            return obj.text[:40] + "..."
        return obj.text
