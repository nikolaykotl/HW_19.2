from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from post.models import Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'body', 'image', 'is_public')
    success_url = reverse_lazy('post:list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)

class PostListView(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_public=True)
        return queryset

class PostDetailView(DetailView):
    model = Post
    slug_field = 'pk'
    slug_url_kwarg = 'pk'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count +=1
        self.object.save()
        return self.object

class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'body', 'image', 'is_public')
   # success_url = reverse_lazy('post:list')
    slug_field = 'pk'
    slug_url_kwarg = 'pk'

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post:view',args=[self.kwargs.get('pk')])
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post:list')
    slug_field = 'pk'
    slug_url_kwarg = 'pk'