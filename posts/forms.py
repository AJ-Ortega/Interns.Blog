from django import forms
from django.forms import fields
from .models import Post, Comment
from django_quill.forms import QuillFormField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')


class QuillFieldForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')
        content = QuillFormField()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'name',)