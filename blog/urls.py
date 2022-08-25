from django.urls import path

from .views import BlogPage

urlpatterns = [
        path('', BlogPage.as_view(), name="home")
        ]

