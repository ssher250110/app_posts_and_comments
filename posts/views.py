from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from posts.models import Post
from posts.permissions import IsAuthor
from posts.serializers import PostSerializer


class PostListCreateAPIView(ListCreateAPIView):
    """Создание поста и просмотр списка постов"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Добавление автора объявления"""

        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Просмотр, изменение и удаление одного поста"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        """Получение прав доступа по условиях"""
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser | IsAuthor]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
