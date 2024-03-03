from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# Using ListView to list all the posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # Default: <app>/<model>_<viewtype>.html

    # To use this name as the context in frontend
    context_object_name = 'posts'

    ordering = ['-date_posted']
    paginate_by = 5  # Posts per page


# Listing all posts by the specific user
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        # Returning the user if exists else 404
        user = get_object_or_404(User, username=self.kwargs.get('username'))

        # Returning all posts by that user with descending (-ve) date ordering
        return Post.objects.filter(author=user).order_by('-date_posted')


# Post details
class PostDetailView(DetailView):
    model = Post


# Create a new post with CreateView
# Login is required to create a new post thus LoginRequiredMixin is used
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # Selecting the present user as the author of this post
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update a post with UpdateView
# Login is required to create a new post thus LoginRequiredMixin is used
# User must pass few tests thus UserPassesTestMixin is used
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        # Logged in user must be the author of this post
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


"""
# *? Post.objects.all() returns a QuerySet that can be imagined this way.
posts = [
    {
        'author': 'John Smith',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 20, 2020'
    },
    {
        'author': 'Eugene T. Bradford',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 22, 2020'
    }
]
"""
