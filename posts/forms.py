from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    model = Post
    fields = ['user', 'title', 'post_picture', 'content']
    widgets = {
        'user': forms.Select(attrs={'class': 'form-control'}),
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'post_picture': forms.FileInput(attrs={'class': 'form-control'}),
        'content': forms.Textarea(attrs={'class': 'form-control'}),
    }
