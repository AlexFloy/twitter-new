import random
from datetime import datetime

from django.utils.crypto import get_random_string
from django.core.management.base import BaseCommand
from posts.models import Post, Comments
from users.models import User


class Command(BaseCommand):
    help = 'Create random users'

    def handle(self, *args, **kwargs):
        for i in range(1, 21):
            User.objects.create(
                user_name=get_random_string(3),
                email=get_random_string(5),
                data_joined=datetime(year=2000 + random.randint(1, 23),
                                     month=1 + random.randint(0, 11),
                                     day=1 + random.randint(0, 29))
            )
        users = User.objects.all()
        for i in range(10):
            Post.objects.create(
                user=random.choice(users),
                title='Example Post',
                content='This is a sample post.'
            )
        posts = Post.objects.all()
        for i in range(1, 5):
            Comments.objects.create(
                user=random.choice(users),
                post=random.choice(posts),
                content='This is a comment on the post.'
            )

        self.stdout.write(self.style.SUCCESS('Успішно створено User, Post і Comment.'))
