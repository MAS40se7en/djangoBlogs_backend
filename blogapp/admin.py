from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Blog
from django.contrib import admin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "profile_image")

admin.site.register(CustomUser, CustomUserAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "is_draft", "category", "created_at")

admin.site.register(Blog, BlogAdmin)