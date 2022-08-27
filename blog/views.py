import logging
from django.views.generic import ListView, DetailView
from .models import BlogNew, NewCategory

logger = logging.getLogger(__name__)

class BlogPage(ListView):
    """Blog Page View with all news."""
    model = BlogNew
    template_name: str = 'blog/index.html'
    context_object_name = 'blog'
    allow_empty: bool = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = NewCategory.objects.all()
        return context

    def get_queryset(self):
        """Return filtered query set."""
        return BlogNew.objects.filter(is_published=True).select_related('category')

class BlogPageOneOfCategory(ListView):
    """BlogPage View with all news for one of them category."""
    model = BlogNew
    template_name: str = "blog/index.html"
    context_object_name = "blog"
    allow_empty: bool = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = NewCategory.objects.get(pk=self.kwargs['pk'])
        #TODO: Обработать ошибку при ручном вводе номера (pk) категории.
        return context

    def get_queryset(self):
        """Return filtered query set."""
        logger.info(f"{self.kwargs}")
        return BlogNew.objects.filter(category_id=self.kwargs['pk'], 
                                      is_published=True).select_related('category')

class ViewNew(DetailView):
    model = BlogNew
    template_name: str = 'blog/view_new.html'
    context_object_name = 'blog_new'




