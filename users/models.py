from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.db.models import TextChoices
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager

NULLABLE = {"blank": True, "null": True}


class UserRoles(TextChoices):
    """Класс для выбора поля role модели User"""

    USER = "user", _("Пользователь")
    ADMIN = "admin", _("Администратор")


class User(AbstractBaseUser):
    """Модель для создания пользователя"""

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        verbose_name="Логин",
        help_text="Укажите логин пользователя",
    )
    password = models.CharField(max_length=128, verbose_name="Пароль", help_text="Укажите пароль")
    email = models.EmailField(unique=True, verbose_name="Почта", help_text="Укажите электронную почту")
    phone = models.CharField(max_length=15, verbose_name="Телефон", help_text="Укажите телефон для связи")
    birth_date = models.DateField(verbose_name="Дата рождения", help_text="Укажите дату рождения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")
    role = models.CharField(
        max_length=5,
        choices=UserRoles,
        default=UserRoles.USER,
        verbose_name="Роль",
        help_text="Укажите роль пользователя",
    )
    is_active = models.BooleanField(
        default=True, verbose_name="Активация", help_text="Укажите активен ли пользователь"
    )
    last_login = models.DateTimeField(_("last login"), **NULLABLE)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone", "birth_date"]

    @staticmethod
    def update_last_login(user, **kwargs):
        user.last_login = timezone.now()
        user.save(update_fields=["last_login"])

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]
