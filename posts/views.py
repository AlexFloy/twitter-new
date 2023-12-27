from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from users.models import User
from django.db.models import Count
from posts.models import Post, Comments, Like
from posts.forms import PostForm, CommentForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from django.shortcuts import get_object_or_404, redirect, reverse
from django.views import View


"""
# def posts_menu(request, user_name=None):
#     if user_name:
#         posts = Post.objects.filter(user__user_name=user_name)
#     else:
#         posts = Post.objects.all()
#
#     context = {'post': posts}
#
#     return render(request, 'posts/posts_list.html', context)
# меню постів, якщо умова надана меню постів юзера
"""


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/posts_list.html'
    extra_context = {'title': 'POSTS LIST'}

    def get_queryset(self):
        if self.kwargs.get('folder'):
            folder = self.kwargs.get('folder')
            if folder == 'my':
                posts = Post.objects.filter(user=self.request.user)
            elif folder == 'follow':
                follower_users = self.request.user.following.all()
                posts = Post.objects.filter(user__in=follower_users)
        else:
            posts = Post.objects.all().select_related('user')
        return posts.annotate(comment_count=Count('comments', distinct=True),
                              like_count=Count('likes', distinct=True))

    def username(self):
        user_name = self.kwargs.get('user_name')
        if user_name:
            return Post.objects.filter(user__user_name=user_name)
        return Post.objects.all()
# меню постів, якщо умова надана меню постів юзера

"""
def comments_menu(request, user_id):
    posts = Post.objects.filter(user__id=user_id)
    post = Post.objects.all()
    users = User.objects.all()
    comment = Comments.objects.filter(user__id=user_id)
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return HttpResponseNotFound
    context = {
        'comment': comment,
        'posts': posts,
        'post': post,
        'user': user,
        'users': users
       }
    return render(request, 'posts/add_comment.html', context)
 меню коментів
"""

"""
# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save()
#             return redirect('posts_detail', post_id=post.pk)
#     else:
#         form = PostForm
#     return render(request, 'posts/create_post.html', {'form': form})
# # додавання посту"""


@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'posts/create_post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#  додавання посту

""""# def post_detail(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     comment = Comments.objects.filter(post__id=post_id)
#     posts = Post.objects.all()
#     context = {
#         'post': post,
#         'posts': posts,
#         'comment': comment
#     }
#     return render(request, 'posts/post_detail.html', context)
# # вигляд посту"""


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/post_detail.html'

    def get_queryset(self):
        posts = Post.objects.all().select_related('user')
        return posts.annotate(comment_count=Count('comments', distinct=True),
                              like_count=Count('likes', distinct=True))

    # зробив select_related, вирішити з юзер

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = Comments.objects.filter(post__id=self.kwargs['pk']).select_related('user').order_by(
            '-create_at')

        return context
# вигляд посту


"""
# def add_comment(request):
#     if request.method == 'POST':
#         comments = CommentForm(request.POST)
#         if comments.is_valid():
#             comment = comments.save()
#             return redirect('posts_detail', post_id=comment.post.pk)
#     else:
#         comments = CommentForm
#     return render(request, 'posts/add_comment.html', {'comments': comments})
# додавання коменту"""


class CommentCreateView(CreateView):
    form_class = CommentForm
    context_object_name = 'comments'
    template_name = 'posts/add_comment.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)
# додавання коменту


def post_like(request, pk):
    user = request.user.pk
    post = get_object_or_404(Post, pk=pk)
    user_instance = User.objects.get(pk=user)

    like, created = Like.objects.get_or_create(user=user_instance, post=post)
    print(f"Like object exists: {like}")

    if user in post.likes.all().values_list('id', flat=True):
        post.likes.remove(user)
        like.value = 'Unlike'
    else:
        post.likes.add(user)
        like.value = 'Like'
    print(f"Before save: {like.value}")  # Додайте цей вивід для відстеження
    like.value = "Unlike" if like.value == "Like" else "Unlike"
    like.save()
    print(f"After save: {like.value}")
    return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'), pk=pk)

# додоавання лайку  доробити !!!!!!!!!
# ставить лайк але не міняє кнопку на unlikee


class PostUpdateView(UpdateView):
    model = Post
    context_object_name = 'update_post'
    template_name = 'posts/post_update.html'

    form_class = PostForm


class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'delete_post'
    template_name = 'posts/delete_post.html'

    def get_success_url(self):
        user_pk = self.request.user.pk

        return reverse_lazy('user_detail', kwargs={'pk': user_pk})

