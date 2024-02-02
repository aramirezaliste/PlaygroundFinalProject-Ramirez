from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

def posts_list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'blog/posts_list.html', context )