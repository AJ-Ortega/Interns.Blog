from django.shortcuts import reverse
from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = QuillField()
    publish_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title
    
    @property
    def get_comment_count(self):
       return self.comment_set.all().count()

    @property
    def comments(self):
        return self.comment_set.all()

    

class Comment(models.Model):
    # user = modelos.ForeingKey()
    name = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user


class PostView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user