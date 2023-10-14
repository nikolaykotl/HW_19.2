from django.contrib import admin

from catalog.models import Product, Category

#admin.site.register(Product)
#admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'purchase_price', 'category', )
    list_filter = ('category',)
    search_fields = ('product_name', 'description_prod', )
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')