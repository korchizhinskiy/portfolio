from django.urls import path

from .views import BlogPage, BlogPageOneOfCategory, home_page, ViewNew

urlpatterns = [
        path('', home_page, name="home"),
        path('blog', BlogPage.as_view(), name="blog"),
        path('blog_new/<int:pk>', ViewNew.as_view(), name="blog_new"),
        path('category/<int:pk>', BlogPageOneOfCategory.as_view(), name="category"),
]

