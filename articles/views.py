
from django.db import models
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class ArticleEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Article
    template_name = "article_edit.html"
    fields = ["title", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url= reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    template_name = "article_create.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user