from django.urls import path

from .views import BlogPage, ViewNew

urlpatterns = [
        path('', BlogPage.as_view(), name="home"),
        path('blog_new/<int:pk>', ViewNew.as_view(), name="blog_new")
        ]

