from django.urls import path

from posts.views import PostListView, PostDetailView, PostCreateView, CommentCreateView, post_like

urlpatterns = [
    path('', PostListView.as_view(), name="posts"),
    path('<str:user_name>', PostListView.as_view(), name="posts_user"),
    path('posts/<int:pk>', PostDetailView.as_view(), name="posts_detail"),
    path('posts/add-comment/<int:pk>', CommentCreateView.as_view(), name="add_comments"),
    path('posts/create-posts', PostCreateView.as_view(), name="create_post"),
    path('posts/like/<int:pk>', post_like, name='posts_like'),
]

