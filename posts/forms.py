from django import forms
from users.models import User
from posts.models import Post, Comments


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['user', 'title', 'posts_picture', 'content']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'posts_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
# 2 view

# 1 view class PostsForm(forms.Form):
#     user = forms.ModelChoiceField(queryset=User.objects.all())
#     title = forms.CharField()
#     posts_picture = forms.ImageField()
#     content = forms.CharField()
#     create_at = forms.DateTimeField()


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['user', 'content']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
