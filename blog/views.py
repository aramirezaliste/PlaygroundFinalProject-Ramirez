from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

def posts_list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'blog/posts_list.html', context)

def create_post(request):
    if request.method == 'GET':
        form = PostForm()
        context = {
            'form': form
        }
    return render(request, 'blog/blog_post_form.html', context)