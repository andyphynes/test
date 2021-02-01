from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
# Create your views here.

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title',  'author', 'haulier', 'material', 'origin', 'destination', 'Vehicle_reg', 'date']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields= ['title', 'haulier', 'material', 'origin', 'destination','Vehicle_reg', 'date']

class BlogDeleteView(DeleteView):
    model =Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')