from django.contrib import admin

from .models import BlogNew, NewCategory


class BlogNewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'reate_date', 'update_date', 'is_published')
    list_display_links = ('id', 'title')

admin.site.register(BlogNew)
admin.site.register(NewCategory)

