from django.urls import path

from posts import views
from posts.views import PostListView, PostDetailView, PostCreateView, CommentCreateView

urlpatterns = [
    path('', PostListView.as_view(), name="posts"),
    path('<str:user_name>', PostListView.as_view(), name="posts_user"),
    path('posts/<int:pk>', PostDetailView.as_view(), name="posts_detail"),
    path('posts/add-comment', CommentCreateView.as_view(), name="add_comments"),
    path('posts/create-posts', PostCreateView.as_view(), name="create_post")

]

