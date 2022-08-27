import logging
from django.views.generic import ListView, DetailView
from .models import BlogNew

logger = logging.getLogger(__name__)

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


class ViewNew(DetailView):
    model = BlogNew
    template_name: str = 'blog/view_new.html'
    context_object_name = 'blog_new'




