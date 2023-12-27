from django.db import models
from users.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.db.models import Sum


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    posts_picture = models.ImageField(upload_to="post/profile_images", null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', default=None, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.user}"

    @property
    def num_likes(self):
        return self.likes.all().count()


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'pk': self.post.pk})

    def __str__(self):
        return f"{self.user} {self.post} {self.content}"






LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES)

    def __str__(self):
        return str(self.post)

