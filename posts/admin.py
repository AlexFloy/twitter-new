from django.contrib import admin

from posts.models import Post, Comments, Like

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Like)
