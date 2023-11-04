from django.urls import path

from posts import views
from posts.views import posts_menu, create_post, add_comment

urlpatterns = [
    path('', posts_menu, name="posts"),
    path('<str:user_name>', posts_menu, name="posts_user"),
    path('posts/<int:post_id>', views.post_detail, name="posts_detail"),
    path('posts/add-comment', add_comment, name="add_comments"),
    path('posts/create-posts', create_post, name="create_post")

]

