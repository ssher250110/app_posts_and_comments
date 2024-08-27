from django.contrib import admin

from posts.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Отображение информации о постах в админ панели"""

    list_display = ["pk", "title", "text", "image", "author", "created_at", "updated_at"]
    list_filter = ["created_at"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Отображение информации о комментариях в админ панели"""

    list_display = ["pk", "text", "post", "author", "created_at", "updated_at"]
    list_filter = ["created_at"]
