from django.urls import path
from users.views import UserListView, UserDetailView, UserUpdateView, subscribe, unsubscribe

urlpatterns = [
    path('', UserListView.as_view(), name="users"),
    path('<str:folder>', UserListView.as_view(), name="users"),
    path('<int:pk>/', UserDetailView.as_view(), name="user_detail"),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
    path('subscribe/<int:pk>/', subscribe, name='subscribe'),
    path('unsubscribe/<int:pk>/', unsubscribe, name='unsubscribe'),
]

