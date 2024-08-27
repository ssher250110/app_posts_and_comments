from rest_framework.serializers import ValidationError


def validate_forbidden_words(value):
    """Валидатор проверки поля заголовок поста"""

    if value.lower() in ["ерунда", "глупость", "чепуха"]:
        raise ValidationError("Использовано запрещенное слово")
