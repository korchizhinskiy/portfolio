from django.shortcuts import render
from .models import BlogNew
from blog.services import get_all_from_database


def index(request):
    news = get_all_from_database(BlogNew)
    return render(request, template_name='blog/index.html', context={"news": news})
