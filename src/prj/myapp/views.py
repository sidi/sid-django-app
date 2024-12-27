from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models.module import *

# Create your views here.

class ModuleListView(ListView):
    model = Module 

class ModuleDetailView(DetailView):
    model = Module 


class ModuleCreateView(CreateView):
    model = Module 
    fields = '__all__'
    success_url = reverse_lazy('module_list')

class ModuleDeleteView(DeleteView):
    model = Module 
    success_url = reverse_lazy('module_list')

class ModuleUpdateView(UpdateView):
    model = Module 
    fields = '__all__'
    success_url = reverse_lazy('module_list')

