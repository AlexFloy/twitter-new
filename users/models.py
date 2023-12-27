from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to="users/profile_images", null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    subscribe = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='following')

    def __str__(self):
        return f"{self.username}"

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})


