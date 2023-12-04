from django.db import models
from users.models import User
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    posts_picture = models.ImageField(upload_to="post/profile_images", null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', default=None, blank=True)

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.user}"

    create_at = models.DateTimeField(auto_now_add=True)

    def add_like(self):
        """
        Додає лайк в список лайків для даного поста
        """
        return self.likes.all().count()


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'pk': self.post.pk})

    def __str__(self):
        return f"{self.user} {self.post} {self.content}"

    create_at = models.DateTimeField(auto_now_add=True)
