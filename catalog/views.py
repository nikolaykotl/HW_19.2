from django.shortcuts import render, redirect
from catalog.models import Product, Category, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from catalog.forms import ProductForm, VersionForm
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
#from django.http import Http404
from django.contrib.auth.mixins import PermissionRequiredMixin
#from django.utils.decorators import method_decorator
#from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from users.mixins import UserRequiredMixin


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    login_url = 'catalog:home'

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(UserRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    login_url = 'catalog:home'
    success_message = 'Успешно изменено'
    permission_required = 'catalog.change_product'

    def get_form_class(self):
        return super().get_form_class()

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST,instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Новое сообщение от {name}({phone}): {message}')
    return render(request, 'catalog/contacts.html')



class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

#def home(request):
  #  product_list = Product.objects.all()
  #  content = {'object_list': product_list}
  #  return render(request, 'catalog/home.html', content)

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        for object in context['product_list']:
            active_version = Version.objects.filter(product=object, is_active=True).last()
            if active_version:
                object.active_version_number = active_version.number
            else:
                object.active_version_number = None
        return context

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