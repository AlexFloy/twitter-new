from django.urls import path
from users import views
from users.views import UserListView, UserDetailView

urlpatterns = [
    path('', UserListView.as_view(), name="users"),
    path('users/<int:pk>', UserDetailView.as_view(), name="user_detail"),
]


