from django.db import models


NULLABLE = {'blank': True, 'null': True}
class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='название продукта')
    description_prod = models.TextField(verbose_name='описание', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    picture = models.ImageField(upload_to='catalog/',verbose_name='изображение', **NULLABLE)
    purchase_price = models.FloatField(verbose_name='стоимость покупки', **NULLABLE)
    date_creation =models.DateField(verbose_name='дата создания', **NULLABLE)
    date_change = models.DateField(verbose_name='дата изменения', **NULLABLE)

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


