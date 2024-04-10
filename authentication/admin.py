from django.contrib import admin

from authentication.models import CustomUser


# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ("username", "email", 'last_login', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'first_name', 'last_name',)

