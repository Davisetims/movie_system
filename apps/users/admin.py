from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone_code", "phone", "created_at")
    search_fields = ("first_name", "last_name", "phone")
    list_filter = ("created_at",)
