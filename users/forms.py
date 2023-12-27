from django import forms
from users.models import User


class UpdateUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'profile_picture']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }
