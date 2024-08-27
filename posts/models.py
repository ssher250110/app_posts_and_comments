from django.conf import settings
from django.db import models

NULLABLE = {"null": True, "blank": True}


class Post(models.Model):
    """Модель поста"""

    title = models.CharField(max_length=50, verbose_name="Название поста", help_text="Укажите название поста")
    text = models.TextField(**NULLABLE, verbose_name="Текст поста", help_text="Укажите текст поста")
    image = models.ImageField(
        upload_to="post/image", **NULLABLE, verbose_name="Изображение", help_text="Загрузите изображение"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Автор Поста",
        help_text="Укажите автора поста",
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    """Модель комментария"""

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Автор комментария",
        help_text="Укажите автора комментария",
    )
    text = models.TextField(verbose_name="Текст комментария", help_text="Добавьте текст комментария")
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, verbose_name="Пост", help_text="Укажите Пост", related_name="comments"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    def __str__(self):
        return self.text[:35]

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
