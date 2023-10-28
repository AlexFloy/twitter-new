from django.urls import path

from posts.views import posts_menu, comments_menu

urlpatterns = [
    path('', posts_menu, name="posts"),
    path('posts/<str:user_name>', posts_menu, name="posts_user"),
    path('comments/', comments_menu, name="comment_menu"),

]