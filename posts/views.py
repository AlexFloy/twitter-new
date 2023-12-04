from django.http import HttpResponse, HttpResponseNotFound

from posts.models import Post, Comments
from posts.forms import PostForm, CommentForm, LikeForm
from django.views.generic import ListView, DetailView, CreateView
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
        query = super().get_queryset()
        return query.select_related('user')

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


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'posts/create_post.html'
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


@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/post_detail.html'

    def get_queryset(self):
        query = super().get_queryset()
        return query.select_related('user')

    # зробив select_related, вирішити з юзер

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = Comments.objects.filter(post__id=self.kwargs['pk']).select_related('user').order_by(
            '-create_at')

        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()

        # Перевірка, чи користувач вже вподобав публікацію
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True

        # Повертаємо JSON-відповідь з інформацією про лайки
        return JsonResponse({'liked': liked, 'likes_count': post.likes.count()})
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
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

# додавання коменту


def add_like(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = LikeForm(request.POST)
        if form.is_valid():
            post.likes.add(request.user)
            post.save()
            return redirect('posts/posts_list.html', pk=pk)
    else:
        form = LikeForm(initial={'post_id': pk})

    return render(request, 'posts/posts_list.html', {'form': form, 'post': post})
