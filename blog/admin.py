from django.contrib import admin

from .models import BlogNew, NewCategory


@admin.register(BlogNew)
class PublicationAdmin(admin.ModelAdmin):
    """Class of publication new in admin site."""
    list_display = ('id', 'title', 'category', 'create_date', 'upgrade_date', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    search_help_text = "Начните вводить заголовок/содержание."


@admin.register(NewCategory)
class CategoryAdmin(admin.ModelAdmin):
    """Class of new category in admin site."""
    list_display = ('pk', 'category_name')
    list_display_links = ('pk', 'category_name')
    search_fields = ('category_name',)
    search_help_text = "Начните вводить название категории."

