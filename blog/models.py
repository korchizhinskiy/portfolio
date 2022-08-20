from django.db import models


class BlogNew(models.Model):
    """Model of new in blog."""
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    content = models.TextField(verbose_name='Контент')
    category = models.ForeignKey(
            to='NewCategory', 
            on_delete=models.PROTECT, 
            verbose_name='Категория')
    create_date = models.DateTimeField(verbose_name='Дата создания', 
                                       auto_now_add=True)
    upgrade_date = models.DateTimeField(verbose_name='Дата обновления', 
                                        auto_now=True,)
    is_published = models.BooleanField(verbose_name='Опубликовано', 
                                       default=True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class NewCategory(models.Model):
    """Model of new category."""
    category_name = models.CharField(
            verbose_name='Категория', 
            max_length=255, 
            unique=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
