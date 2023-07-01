from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post, Comment
from users.models import GeekUser
from django.views import generic
from django.urls import reverse_lazy
from blog.forms import CommentForm, PostForm
from blog.serializers import PostSerializer, PostDetailSerializer, CommentSerializer, \
    UsersSerializer, UsersDetailSerializer
from rest_framework import generics


class UsersListAPIView(generics.ListAPIView):
    serializer_class = UsersSerializer
    queryset = GeekUser.objects.all()


class UsersDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UsersDetailSerializer
    queryset = GeekUser.objects.all()
    lookup_field = 'id'


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


class PostDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'


class CommentAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post'])


# Create your views here.

class IndexListView(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status=True)
    context_object_name = "posts"
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"
    lookup_field = 'pk'

    # extra_context = {"form": CommentForm()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            pre_saved_comment = form.save(commit=False)
            pre_saved_comment.post = post
            pre_saved_comment.save()
        return redirect('post-detail', pk)

    """def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        username = request.POST.get('username')
        text = request.POST.get('comment_text')
        if username and text:
            comment = Comment.objects.create(username=username, text=text, post=post)
            comment.save()
        return redirect('post-detail', pk)"""


# --------------- Create some objects in databases ------------------

class PostCreateView(generic.CreateView):
    model = Post
    template_name = "blog/post_create.html"
    # fields = ["title", "content", "cover"]
    form_class = PostForm
    success_url = reverse_lazy('index-page')


# --------------- Delete -------------------------

class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('index-page')


# ----------------- Update --------------------------------
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
