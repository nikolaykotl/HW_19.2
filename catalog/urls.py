from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product, category

app_name = CatalogConfig.name
urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('category/', category),
    path('<int:id>/product/', product, name='product')
]