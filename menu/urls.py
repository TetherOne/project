"""
URL configuration for menu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static

from django.conf import settings
from django.contrib import admin

from django.urls import include
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/favoritesapp/", include("favorites.urls")),
    path("api/v1/commentsapp/", include("comments.urls")),
    path("api/v1/profilesapp/", include("profiles.urls")),
    path("api/v1/dishesapp/", include("dishes.urls")),
    path("api/v1/cartapp/", include("cart.urls")),
    path("api/v1/auth/", include("authentication.urls")),
]


urlpatterns.extend(
    static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
)
