from rest_framework.serializers import ValidationError


class PasswordValidator:
    """Валидатор проверки поля пароль"""

    def __init__(self, field):
        self.field = field

    def __call__(self, user):
        password: str = user.get(self.field)
        if len(password) < 8:
            raise ValidationError("Пароль должен быть не менее 8 символов")
        elif not any(el.isdigit() for el in password):
            raise ValidationError("Пароль должен включать буквы и цифры")


class EmailValidator:
    """Валидатор проверки поля почта"""

    def __init__(self, field):
        self.field = field

    def __call__(self, user):
        email: str = user.get(self.field)
        if not email.endswith(("mail.ru", "yandex.ru")):
            raise ValidationError("Разрешены домены: mail.ru, yandex.ru")
