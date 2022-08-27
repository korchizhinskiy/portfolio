from django.urls import path

from .views import BlogPage, BlogPageOneOfCategory, ViewNew

urlpatterns = [
        path('', BlogPage.as_view(), name="home"),
        path('blog_new/<int:pk>', ViewNew.as_view(), name="blog_new"),
        path('category/<int:pk>', BlogPageOneOfCategory.as_view(), name="category"),
]

