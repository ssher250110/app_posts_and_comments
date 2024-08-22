from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    """Проверка прав доступа владельца к контроллеру объекта"""

    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True
        return False
