from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserViewSet

users_router = SimpleRouter()
users_router.register("users", UserViewSet, basename="users")

app_name = UsersConfig.name

urlpatterns = [
    path("", include(users_router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("refresh/", TokenRefreshView.as_view(), name="token"),
]
