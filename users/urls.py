from django.urls import path

from users.views import users

urlpatterns = [
    path('', users, name="users")
]


