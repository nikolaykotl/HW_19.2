from django.contrib import admin


from catalog.models import Product, Category, Version


#admin.site.register(Product)
#admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'purchase_price', 'category', 'description_prod', 'is_published', )
    list_filter = ('category','is_published',)
    search_fields = ('product_name', 'description_prod', 'is_published',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if request.user.is_superuser:
            return form

        elif request.user.is_staff:
            form.base_fields['product_name'].disabled = True
            form.base_fields['purchase_price'].disabled = True
            form.base_fields['owner'].disabled = True
            return form


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number', 'name', 'is_active')
    list_filter = ('is_active',)