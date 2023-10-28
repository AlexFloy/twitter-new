from django.shortcuts import render, redirect
from django.http import HttpResponse

from users.models import User
from posts.models import Post, Comments
from posts.forms import PostForm


def posts_menu(request, user_name=None):
    if user_name:
        posts = Post.objects.filter(user__user_name=user_name)
    else:
        posts = Post.objects.all()

    context = {'post': posts}

    return render(request, 'posts/posts_list.html', context)
# меню постів, якщо умова надана меню постів юзера


def comments_menu(request):
    comment = Comments.objects.all()
    context = {'comments': comment}
    return render(request, 'posts/comments_menu.html', context)
# меню коментів


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('posts_list', post_id=post.pk)
    else:
        form = PostForm
    return render(request, 'posts/create_post2.html', {'form': form})
# додавання посту



