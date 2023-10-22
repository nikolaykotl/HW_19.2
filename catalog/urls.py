from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, category, ProductListView, ProductDetailView, CategoryListView

app_name = CatalogConfig.name
urlpatterns = [
    path('',ProductListView.as_view() , name='home'),
    path('contacts/', contacts),
    path('category/', CategoryListView.as_view(), name='category'),
    path('<slug:id>/product/', ProductDetailView.as_view(), name='product')
]