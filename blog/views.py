from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogNew
from blog.services import get_all_from_database


class BlogPage(ListView):
    """Blog Page View with all news."""
    model = BlogNew
    template_name: str = 'blog/index.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Блог'
        return context

    def get_queryset(self):
        """Return filtered query set."""
        return BlogNew.objects.filter(is_published=True)
