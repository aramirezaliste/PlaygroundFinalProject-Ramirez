from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

def posts_list(request):
    posts = Post.objects.all()
    posts_len = len(posts)
    context = {
        'posts' : posts,
        'posts_len' : posts_len
    }
    return render(request, 'blog/posts_list.html', context)

def create_post(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save()
                post.author = user
                post.save()
        else:
            return redirect("blog:index")
        return redirect("blog:posts_list")
    else: #request.method == 'GET':
        form = PostForm()
        user = None
        if request.user.is_authenticated:
            user = request.user
            print(user.id)
        else:
            user = None
        context = {
            'form': form,
            'user': user
        }
    return render(request, 'blog/blog_post_form.html', context)