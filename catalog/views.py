from django.shortcuts import render
from catalog.models import Product, Category

def home(request):
    product_list = Product.objects.all()
    content = {'object_list': product_list}
    return render(request, 'catalog/home.html', content)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Новое сообщение от {name}({phone}): {message}')
    return render(request, 'catalog/contacts.html')


def product(request, id):
   object = Product.objects.get(pk=id)
   content = {'object': object}
   return render(request, 'catalog/product.html', content)


def category(request):
    content = {
        'category_list': Category.objects.all(),
        'title': 'Категории товаров'
    }
    return render(request, 'catalog/category.html', content)