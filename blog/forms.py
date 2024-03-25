from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from .models import blog
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment')


class PostForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ('title', 'description', 'image', 'content', 'keywords')

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')