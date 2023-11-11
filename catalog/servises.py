from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_cache_category_list():
    if settings.CACHE_ENABLE:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
        else:
            category_list = Category.objects.all()
        return category_list