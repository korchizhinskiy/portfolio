from django import template

from blog.models import BlogNew

register = template.Library()


@register.simple_tag()
def get_categories():
    return BlogNew.objects.select_related('category').distinct('category').filter(is_published=True)

