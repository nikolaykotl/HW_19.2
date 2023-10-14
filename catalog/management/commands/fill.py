from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'category_name': 'Гаджеты', 'description_cat': 'Телефоны, смартфоны и т.п.'},
            {'category_name': 'Техника для кухни', 'description_cat': 'Все для кухни'},
            {'category_name': 'Аудиотехника', 'description_cat': 'Все для прослушивания аудио'}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_for_create)