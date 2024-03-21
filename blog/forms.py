from django import forms

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