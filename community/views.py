from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import ClassPost

class PostView(ListView):
    template_name = 'community/list.html'
    context_object_name = 'post_list'
    model = ClassPost


class PostCreate(CreateView):
    model = ClassPost
    fields = ["title", "body"]
    success_url = reverse_lazy('list')


class PostRead(DetailView):
    context_object_name = 'post'
    model = ClassPost
    

class PostUpdate(UpdateView):
    model = ClassPost
    fields = ["title", "body"]
    success_url = reverse_lazy("list")


class PostDelete(DeleteView):
    model = ClassPost
    success_url = reverse_lazy("list")