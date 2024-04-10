from django.urls import path

from authentication.views import CurrentUserView

app_name = "authentication"


urlpatterns = [
    path(
        "current-user/",
        CurrentUserView.as_view(),
        name="current-user",
    ),
]