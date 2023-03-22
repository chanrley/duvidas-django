from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Usuario
from django.urls import  reverse_lazy
import logging

# logger = logging.getLogger('django')

# Nova maneira de CRUD usando Class Based Views(CBV) em vez de Functions Based Views(FBV)
class UsuarioList(ListView):
    model: Usuario
    queryset = Usuario.objects.all()

class UsuarioCreate(CreateView):
    
    model = Usuario
    fields = '__all__'
    # logger.info('INFO usuario criado')
    success_url = reverse_lazy('usuario:list')

class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = '__all__'
    success_url = reverse_lazy('usuario:list')

class UsuarioDetail(DetailView):
    queryset = Usuario.objects.all()


class UsuarioDelete(DeleteView):
    queryset = Usuario.objects.all()
    success_url = reverse_lazy('usuario:list')

