from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from . import models

# Create your views here.

class ModuleListView(ListView):
    model = models.Module 

class ModuleDetailView(DetailView):
    model = models.Module 


class ModuleCreateView(CreateView):
    model = models.Module 
    fields = '__all__'
    success_url = reverse_lazy('module_list')

class ModuleDeleteView(DeleteView):
    model = models.Module 
    success_url = reverse_lazy('module_list')

class ModuleUpdateView(UpdateView):
    model = models.Module 
    fields = '__all__'
    success_url = reverse_lazy('module_list')

