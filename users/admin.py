from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
        "email",
        "phone",
        "birth_date",
        "created_at",
        "updated_at",
        "role",
        "is_active",
        "last_login",
    ]
