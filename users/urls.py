from django.urls import path
from users.views import UserListView, UserDetailView, post_like

urlpatterns = [
    path('', UserListView.as_view(), name="users"),
    path('users/<int:pk>/', UserDetailView.as_view(), name="user_detail"),
    path('users/like/<int:pk>/', post_like, name='post_like'),
]

