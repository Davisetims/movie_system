from django.contrib import admin
from .models import Category, ScreenRole

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(ScreenRole)
class ScreenRoleAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
