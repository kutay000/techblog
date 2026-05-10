from django import forms
from .models import Post, Comment

# 📝 POST FORM
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


# 💬 COMMENT FORM
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']