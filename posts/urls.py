from django.urls import path

from posts.apps import PostsConfig
from posts.views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

app_name = PostsConfig.name

urlpatterns = [
    path("posts/", PostListCreateAPIView.as_view(), name="posts-list-create"),
    path("posts/<pk:int>/", PostRetrieveUpdateDestroyAPIView.as_view(), name="posts-retrieve-update-destroy"),
]