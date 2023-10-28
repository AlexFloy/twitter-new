from django.db import models
from users.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    posts_picture = models.ImageField(upload_to="post/profile_images", null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user}"

    create_at = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"{self.user} {self.post} {self.content}"

    create_at = models.DateTimeField(auto_now_add=True)
