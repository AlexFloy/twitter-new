from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=35)
    email = models.EmailField(max_length=254, unique=True)
    profile_picture = models.ImageField(upload_to="users/profile_images", null=True, blank=True)
    data_joined = models.DateField()

    def __str__(self):
        return f"{self.user_name}"

    create_at = models.DateTimeField(auto_now_add=True)
