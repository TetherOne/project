from django.contrib import admin

from profiles.models import ClientProfile


@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):

     list_display = ("name", "surname", "father_name")