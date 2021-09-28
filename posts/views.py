from django.shortcuts import render , redirect
from django.views.generic import ListView, DetailView, CreateView 
from .models import Post, PostView, Comment
from .forms import PostForm, QuillFieldForm, CommentForm
# Create your views here.

def post_form(request):
    return render(request, 'post_form.html', {'form': QuillFieldForm()})

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.post = post
            comment.save()
            return redirect("detail", post.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form' : CommentForm()
        })
        return context

class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update ({
            'view_type': 'create'
        })
        return context
