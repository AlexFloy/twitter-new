from django.shortcuts import render
from django.http import HttpResponseNotFound

from users.models import User
from posts.models import Post


def users(request):
    user = User.objects.all()
    context = {'user': user}
    return render(request, "users/user_list.html", context)


def user_detail(request, user_id):
    posts = Post.objects.filter(user__id=user_id)
    post = Post.objects.all()
    users = User.objects.all()
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return HttpResponseNotFound
    context = {
        'user': user,
        'posts': posts,
        'users': users,
        'post': post,
    }
    return render(request, "users/user_detail.html", context)
