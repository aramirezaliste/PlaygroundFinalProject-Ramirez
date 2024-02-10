from django.contrib import admin
from .models import CustomUser

admin.site.site_title = "Users"

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username","first_name", "last_name", "email", "link", "description")
    list_display_links = ("first_name",)
    search_fields = ("first_name",)
    ordering = ("username", "first_name")
    list_filter = ("username",)

admin.site.register(CustomUser, CustomUserAdmin)