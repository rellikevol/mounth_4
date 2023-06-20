from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.

class IndexListView(generic.ListView):
    #model = Post
    queryset = Post.objects.filter(status=True)
    context_object_name = "posts"
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"
    lookup_field = 'pk'

#--------------- Create some objects in databases ------------------

class PostCreateView(generic.CreateView):
    model = Post
    template_name = "blog/post_create.html"
    fields = ["title", "content", "cover"]
    success_url = reverse_lazy('index-page')

#--------------- Delete -------------------------

class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('index-page')

#----------------- Update --------------------------------
class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    fields = ["title", "content", "cover"]
    success_url = reverse_lazy('index-page')

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
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_delete.html', {"post": post})
