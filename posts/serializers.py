from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer

from posts.models import Post, Comment


class CommentSerializer(ModelSerializer):
    """Сериализатор комментария"""

    author = ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ["pk", "text", "post", "created_at", "updated_at", "author"]


class PostSerializer(ModelSerializer):
    """Сериализатор поста"""

    comments = CommentSerializer(many=True, read_only=True)
    author = ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ["pk", "title", "text", "image", "created_at", "updated_at", "author", "comments"]
