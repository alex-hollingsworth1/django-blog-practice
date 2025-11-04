"""
Blog views for handling blog post display and management.

This module contains views for displaying blog posts including:
- The starting page with the latest 3 posts
- A list of all posts
- Individual post details with associated tags
"""

from django.views.generic import ListView, DetailView

from .models import Post
from .forms import CommentForm


class StartingPageView(ListView):
    """Display the starting page with the 3 most recent blog posts."""

    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        """Return the 3 most recent blog posts."""
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    """Display a list of all blog posts in reverse chronological
    order."""

    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


class SinglePostView(DetailView):
    """Display detailed view of a single blog post with its associated
    tags."""

    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        """Add the post's tags to the context."""
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context
