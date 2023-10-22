from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    body = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='post/', verbose_name='изображение', **NULLABLE)
    create_date = models.DateField(auto_now_add=True, verbose_name='дата создания', **NULLABLE)
    is_public = models.BooleanField(default=True, verbose_name='опубликован')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'