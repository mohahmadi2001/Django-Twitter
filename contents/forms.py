from django import forms
from .models import Post,Comment


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'user', 'status', 'tags']

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'status', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'user', 'related_post', 'reply_to']


