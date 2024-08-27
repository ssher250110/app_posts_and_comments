from rest_framework.serializers import ModelSerializer

from posts.validators import AgeValidator
from users.models import User
from users.validators import PasswordValidator, EmailValidator


class UserSerializers(ModelSerializer):
    """Сериализатор пользователя"""

    class Meta:
        model = User
        fields = ["pk", "username", "password", "email", "phone", "birth_date"]
        extra_kwargs = {"password": {"write_only": True}}
        validators = [
            PasswordValidator(field="password"),
            EmailValidator(field="email"),
            AgeValidator(field="birth_date"),
        ]

    def create(self, validated_data):
        """Сохранение объекта"""
        return User.objects.create_user(**validated_data)
