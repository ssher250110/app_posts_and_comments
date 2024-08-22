from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Менеджер объекта для создания пользователя и суперпользователя"""

    def create_user(self, username, email, phone, birth_date, password=None, role="user"):
        """Функция создания пользователя"""
        if not username:
            raise ValueError("У пользователя должен быть login")
        if not email:
            raise ValueError("У пользователя должен быть адрес электронной почты")
        user = self.model(
            username=username,
            email=email,
            phone=phone,
            birth_date=birth_date,
            role=role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone, birth_date, password=None, role="admin"):
        """Функция создания суперпользователя — с ее помощью мы создаем администратора,
        с помощью команды createsuperuser"""

        user = self.create_user(
            username,
            email=email,
            phone=phone,
            birth_date=birth_date,
            password=password,
            role=role,
        )
        user.save(using=self._db)
        return user
