from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from users.models import User
from posts.models import Post, Comments
from posts.forms import PostForm, CommentForm


def posts_menu(request, user_name=None):
    if user_name:
        posts = Post.objects.filter(user__user_name=user_name)
    else:
        posts = Post.objects.all()

    context = {'post': posts}

    return render(request, 'posts/posts_list.html', context)
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


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('posts_detail', post_id=post.pk)
    else:
        form = PostForm
    return render(request, 'posts/create_post2.html', {'form': form})
# додавання посту


# def create_post(request):
#     if request.method == 'POST':
#         form = PostsForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = Post.objects.create(**form.cleaned_data)
#             return redirect('posts_detail', post_id=post.pk)
#     else:
#         form = PostsForm()
#         return render(request, 'posts/create_post2.html', {'form': form})

# def get_post(request):
#     posts = Post.object.all()
#     content = {
#         'post': posts
#     }
#     return render(request, 'posts/post_detail.html', content)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = Comments.objects.filter(post__id=post_id)
    posts = Post.objects.all()
    context = {
        'post': post,
        'posts': posts,
        'comment': comment
    }
    return render(request, 'posts/post_detail.html', context)
# вигляд посту


def add_comment(request):
    if request.method == 'POST':
        comments = CommentForm(request.POST)
        if comments.is_valid():
            comment = comments.save()
            return redirect('posts_detail', post_id=comment.pk)
    else:
        comments = CommentForm
    return render(request, 'posts/add_comment.html', {'comments': comments})
# додавання коменту