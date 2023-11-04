from django.urls import path
from users import views
from users.views import users, user_detail

urlpatterns = [
    path('', users, name="users"),
    path('users/<int:user_id>/', views.user_detail, name="user_detail"),
]


