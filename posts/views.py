from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from posts.models import Post, Comment
from posts.permissions import IsAuthor
from posts.serializers import PostSerializer, CommentSerializer


class PostListCreateAPIView(ListCreateAPIView):
    """Создание поста и просмотр списка постов"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Добавление автора поста"""

        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Просмотр, изменение и удаление одного поста"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        """Получение прав доступа по условиям"""

        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser | IsAuthor]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class CommentViewSet(ModelViewSet):
    """Набор связанных представлений модели комментарий"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        """Добавление автора комментария"""

        serializer.save(author=self.request.user)

    def get_permissions(self):
        """Получение прав доступа по условиям"""

        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["retrieve", "list"]:
            self.permission_classes = [IsAuthenticated]
        elif self.action == ["destroy", "update"]:
            self.permission_classes = [IsAdminUser | IsAuthor]
        return super().get_permissions()
