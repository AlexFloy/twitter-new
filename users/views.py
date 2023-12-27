from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect

from users.models import User
from users.forms import UpdateUser
from posts.models import Post, Comments, Like
from django.db.models import Count
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import get_user_model
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

    def get_queryset(self):
        folder = self.kwargs.get('folder')

        if folder == 'subscribe':
            queryset = self.request.user.subscribe.all()
        elif folder == 'following':
            queryset = self.request.user.following.all()
        else:
            queryset = User.objects.all()

        return queryset
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

    def get_queryset(self):
        return super().get_queryset().annotate(
            subscribes_count=Count('subscribe', distinct=True),
            following_count=Count('following', distinct=True))

    def get_context_data(self, **kwargs):
        post = super().get_context_data(**kwargs)
        user = User.objects.get(pk=self.kwargs['pk'])
        post['posts'] = Post.objects.filter(user=user).annotate(
            comment_count=Count('comments', distinct=True),
            like_count=Count('likes', distinct=True))
        post['subscribe'] = user.subscribe.all().select_related('user')
        post['following'] = user.following.all().select_related('user')

        return post


class UserUpdateView(UpdateView):
    model = User
    context_object_name = 'update_user'
    template_name = 'users/user_update.html'

    form_class = UpdateUser


def subscribe(request, pk):
    user_subscribe = get_object_or_404(User, pk=pk)
    request.user.following.add(user_subscribe)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unsubscribe(request, pk):
    user_unsubscribe = get_object_or_404(User, pk=pk)
    request.user.following.remove(user_unsubscribe)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

