from django.shortcuts import render
from catalog.models import Product, Category
from django.views.generic import ListView, DetailView

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

#def home(request):
  #  product_list = Product.objects.all()
  #  content = {'object_list': product_list}
  #  return render(request, 'catalog/home.html', content)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Новое сообщение от {name}({phone}): {message}')
    return render(request, 'catalog/contacts.html')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
#def product(request, id):
 #  object = Product.objects.get(pk=id)
  # content = {'object': object}
   #return render(request, 'catalog/product.html', content)

class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category.html'
def category(request):
    content = {
        'category_list': Category.objects.all(),
        'title': 'Категории товаров'
    }
    return render(request, 'catalog/category.html', content)