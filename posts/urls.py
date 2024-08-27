from django.urls import path, include
from rest_framework.routers import SimpleRouter

from posts.apps import PostsConfig
from posts.views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, CommentViewSet

comment_router = SimpleRouter()
comment_router.register("comments", CommentViewSet, basename="comments")

app_name = PostsConfig.name

urlpatterns = [
    path("posts/", PostListCreateAPIView.as_view(), name="posts-list-create"),
    path("posts/<int:pk>/", PostRetrieveUpdateDestroyAPIView.as_view(), name="posts-retrieve-update-destroy"),
    path("", include(comment_router.urls)),
]
