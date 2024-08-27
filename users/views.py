from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import IsUser
from users.serializers import UserSerializers


class UserViewSet(ModelViewSet):
    """Контроллер действий с пользователем"""

    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_permissions(self):
        """Функция разрешений на определенные действия, в зависимости от роли пользователя"""
        if self.action == "create":
            self.permission_classes = [AllowAny]
        elif self.action in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["update", "partial_update"]:
            self.permission_classes = [IsAdminUser | IsUser]
        elif self.action == "destroy":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
