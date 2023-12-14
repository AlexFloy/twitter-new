from django.shortcuts import render
from django.http import HttpResponseNotFound

from users.models import User
from posts.models import Post, Like
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect

"""
# def users(request):
#     user = User.objects.all()
#     context = {'user': user}
#     return render(request, "users/user_list.html", context)
#"""


class UserListView(ListView):
    model = User
    context_object_name = 'user_info'
    template_name = 'users/user_list.html'
    extra_context = {'title': 'USER LIST'}
    paginate_by = 9

"""
# def user_detail(request, user_id):
#     posts = Post.objects.filter(user__id=user_id)
#     post = Post.objects.all()
#     users = User.objects.all()
#     try:
#         user = User.objects.get(pk=user_id)
#     except User.DoesNotExist:
#         return HttpResponseNotFound
#     context = {
#         'user': user,
#         'posts': posts,
#         'users': users,
#         'post': post,
#     }
#     return render(request, "users/user_detail.html", context)
"""


class UserDetailView(DetailView):
    model = User
    context_object_name = 'user_info'
    template_name = 'users/user_detail.html'

    # def get_queryset(self):
    #     query = super().get_queryset()
    #     return query.prefetch_related('id')

    def get_context_data(self, **kwargs):
        post = super().get_context_data(**kwargs)
        post['posts'] = Post.objects.filter(user=post['user_info']).select_related('user')
        return post


