from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializers(ModelSerializer):
    """Сериализатор пользователя"""

    class Meta:
        model = User
        fields = ["username", "password", "email", "phone", "birth_date"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """Сохранение объекта"""
        return User.objects.create_user(**validated_data)
