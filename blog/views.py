import logging
from django.http.response import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import BlogNew, NewCategory

logger = logging.getLogger(__name__)


def home_page(request):
    """View home page."""
    return render(request, 'blog/index.html')


class BlogPage(ListView):
    """Blog Page View with all news."""
    model = BlogNew
    template_name: str = 'blog/blog.html'
    context_object_name = 'blog'
    allow_empty: bool = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = NewCategory.objects.all()
        return context

    def get_queryset(self):
        """Return filtered query set."""
        return BlogNew.objects.order_by('-create_date').filter(is_published=True).select_related('category')

class BlogPageOneOfCategory(ListView):
    """BlogPage View with all news for one of them category."""
    model = BlogNew
    template_name: str = "blog/blog.html"
    context_object_name = "blog"
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['title'] = NewCategory.objects.get(pk=self.kwargs['pk'])
        except NewCategory.DoesNotExist:
            raise Http404()
        return context

    def get_queryset(self):
        """Return filtered query set."""
        return BlogNew.objects.filter(category_id=self.kwargs['pk'], 
                                      is_published=True).select_related('category')

class ViewNew(DetailView):
    """View one of news by click on 'Read more'."""
    model = BlogNew
    template_name: str = 'blog/view_new.html'
    context_object_name = 'blog_new'




