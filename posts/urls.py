from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView


urlpatterns = [
    path("list/", PostListView.as_view(), name="post_list"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("new/", PostCreateView.as_view(), name="post_new")
]