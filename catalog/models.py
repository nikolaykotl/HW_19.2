from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from config import settings

NULLABLE = {'blank': True, 'null': True}
class Product(models.Model):
    product_name = models.CharField(max_length=180, verbose_name='название продукта')
    description_prod = models.TextField(verbose_name='описание', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    picture = models.ImageField(upload_to='catalog/',verbose_name='изображение', **NULLABLE)
    purchase_price = models.FloatField(verbose_name='стоимость покупки', **NULLABLE)
    date_creation =models.DateField(auto_now_add=True, verbose_name='дата создания', **NULLABLE)
    date_change = models.DateField(auto_now_add=True, verbose_name='дата изменения', **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{self.product_name};\n' \
               f'Описание: {self.description_prod}\n' \
               f'Цена: {self.purchase_price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)

class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='название категории')
    description_cat = models.TextField(verbose_name='описание', **NULLABLE)
  #  create_at = models.CharField(max_length=10, **NULLABLE)

    def __str__(self):
        return f'{self.id}: {self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)
class Version(models.Model):

    VERSION = [(True, 'активная'), (False, 'не активная'),]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number = models.CharField(max_length=5, verbose_name='номер версии', **NULLABLE)
    name = models.CharField(max_length=50, verbose_name='название версии', **NULLABLE)
    is_active = models.BooleanField(choices=VERSION, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product} {self.number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('number',)


@receiver(post_save, sender=Version)
def set_current_version(sender, instance, **kwargs):
    if instance.is_active:
        Version.objects.filter(product=instance.product).exclude(pk=instance.pk).update(is_active=False)