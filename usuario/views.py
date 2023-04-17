from django.shortcuts import render, HttpResponse
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

############################
#Tentando importar usuários#
############################
from django.http import JsonResponse
from csv import reader
# from django.contrib.auth.models import User
from .models import Usuario

def userdata(request):
    with open('usuario/file.csv', 'r') as csv_file:
        csvf = reader(csv_file)
        data = []
        for drt, nome, cargo, perfil_acesso in csvf:
            drt = Usuario(drt=drt)
            nome = Usuario(nome=nome)
            cargo = Usuario(cargo=cargo)
            perfil_acesso = Usuario(perfil_acesso=perfil_acesso)
            
            data.append(drt, nome, cargo, perfil_acesso)
        Usuario.ojects.bulk_create(data)
    
    return JsonResponse('user csv is now working', safe=False)


############################
import pandas as pd
# from .models import Usuario
from usuario.models import Usuario
# import usuario.Usuario

def importar(request):
    tmp_data=pd.read_csv('usuario/file.csv',sep=';')
    #ensure fields are named~ID,Product_ID,Name,Ratio,Description
    #concatenate name and Product_id to make a new field a la Dr.Dee's answer
    usuarios = [
        Usuario(
            drt = tmp_data['drt'],
            nome = tmp_data['nome'],
            cargo = tmp_data['cargo'],
            perfil_acesso = tmp_data['perfil_acesso'],

            # description = tmp_data.ix[row]['Description'],
            # price = tmp_data.ix[row]['price'],
        )
        for row in tmp_data['drt']
    ]
    Usuario.objects.bulk_create(usuarios)
    return HttpResponse("Funcionou!!!")

