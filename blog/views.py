from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post


# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'blog/index.html', context=context)

def get_post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {"post": post})


def get_contacts(request):
    return render(request, 'blog/contacts.html')


def get_about(request):
    return render(request, 'blog/about.html')

def post_update(request, pk):
    return render(request, 'blog/post_update.html')

def post_delete(request, pk):
    return render(request, 'blog/post_delete.html')