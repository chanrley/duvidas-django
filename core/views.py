from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from item.models import Category, Item
# from .forms import SignupForm, LogadoForm, LoginForm, UsuarioModelForm, LoginModelForm, UsuarioModelForm2
from django.db import models
from novo_portal_dva.models import models, Menu, SubMenu
# from core.models import Usuario
from django.contrib import messages
from usuario.models import Usuario
from core.forms import UsuarioModelForm


def index(request):
    menus = Menu.objects.all()
    submenus = SubMenu.objects.all()

    return render(request, 'core/index.html', {
        'menus': menus,
        'submenus': submenus,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def nova_url(request):
    categories = Category.objects.all()
    return render(request, 'core/nova_url.html', {
        'categories': categories
    })

def master(request):
    categories = Category.objects.all()
    return render(request, 'core/master.html', {
        'categories': categories
    })

def navbar(request):
    menus = Menu.objects.all()
    submenus = SubMenu.objects.all()
    id = 1
    subs = SubMenu.objects.filter(menu_id=id).values()
    um = SubMenu.objects.filter(menu_id=1).values()
    dois = SubMenu.objects.filter(menu_id=2).values()
    tres = SubMenu.objects.filter(menu_id=3).values()
    quatro = SubMenu.objects.filter(menu_id=4).values()
    cinco = SubMenu.objects.filter(menu_id=5).values()
    seis = SubMenu.objects.filter(menu_id=6).values()
    sete = SubMenu.objects.filter(menu_id=7).values()
    oito = SubMenu.objects.filter(menu_id=8).values()
    nove = SubMenu.objects.filter(menu_id=9).values()
    dez = SubMenu.objects.filter(menu_id=10).values()
    onze = SubMenu.objects.filter(menu_id=11).values()
    doze = SubMenu.objects.filter(menu_id=12).values()
    treze = SubMenu.objects.filter(menu_id=13).values()
    quatorze = SubMenu.objects.filter(menu_id=14).values()
    quinze = SubMenu.objects.filter(menu_id=15).values()
    dezesseis = SubMenu.objects.filter(menu_id=16).values()
    dezessete = SubMenu.objects.filter(menu_id=17).values()
    dezoito = SubMenu.objects.filter(menu_id=18).values()
    dezenove = SubMenu.objects.filter(menu_id=19).values()
    vinte = SubMenu.objects.filter(menu_id=20).values()


    return render(request, 'core/navbar.html', {
        'menus': menus,
        'submenus': submenus,
        'subs': subs,
        'um': um,
        'dois': dois,
        'tres': tres,
        'quatro': quatro,
        'cinco': cinco,
        'seis': seis,
        'sete': sete,
        'oito': oito,
        'nove': nove,
        'dez': dez,
        'onze': onze, 	
        'doze': doze,	
        'treze': treze,	
        'quatorze': quatorze,
        'quinze': quinze,
        'dezesseis': dezesseis,
        'dezessete': dezessete,
        'dezoito': dezoito,
        'dezenove': dezenove, 
        'vinte': vinte,
    })

def navbar_novo_layout(request):
    menus = Menu.objects.all()
    submenus = SubMenu.objects.all()
    um = SubMenu.objects.filter(menu_id=1).values()
    dois = SubMenu.objects.filter(menu_id=2).values()
    tres = SubMenu.objects.filter(menu_id=3).values()
    quatro = SubMenu.objects.filter(menu_id=4).values()
    cinco = SubMenu.objects.filter(menu_id=5).values()
    seis = SubMenu.objects.filter(menu_id=6).values()
    sete = SubMenu.objects.filter(menu_id=7).values()
    oito = SubMenu.objects.filter(menu_id=8).values()
    nove = SubMenu.objects.filter(menu_id=9).values()
    dez = SubMenu.objects.filter(menu_id=10).values()
    onze = SubMenu.objects.filter(menu_id=11).values()
    doze = SubMenu.objects.filter(menu_id=12).values()
    treze = SubMenu.objects.filter(menu_id=13).values()
    quatorze = SubMenu.objects.filter(menu_id=14).values()
    quinze = SubMenu.objects.filter(menu_id=15).values()
    dezesseis = SubMenu.objects.filter(menu_id=16).values()
    dezessete = SubMenu.objects.filter(menu_id=17).values()
    dezoito = SubMenu.objects.filter(menu_id=18).values()
    dezenove = SubMenu.objects.filter(menu_id=19).values()
    vinte = SubMenu.objects.filter(menu_id=20).values()


    return render(request, 'core/navbar_novo_layout.html', { 
        'menus': menus,
        'um': um,
        'dois': dois,
        'tres': tres,
        'quatro': quatro,
        'cinco': cinco,
        'seis': seis,
        'sete': sete,
        'oito': oito,
        'nove': nove,
        'dez': dez,
        'onze': onze, 	
        'doze': doze,	
        'treze': treze,	
        'quatorze': quatorze,
        'quinze': quinze,
        'dezesseis': dezesseis,
        'dezessete': dezessete,
        'dezoito': dezoito,
        'dezenove': dezenove, 
        'vinte': vinte,
    
    })

def navbar_novo_layout_integrado(request):
    menus = Menu.objects.all()
    submenus = SubMenu.objects.all()
    um = SubMenu.objects.filter(menu_id=1).values()
    dois = SubMenu.objects.filter(menu_id=2).values()
    tres = SubMenu.objects.filter(menu_id=3).values()
    quatro = SubMenu.objects.filter(menu_id=4).values()
    cinco = SubMenu.objects.filter(menu_id=5).values()
    seis = SubMenu.objects.filter(menu_id=6).values()
    sete = SubMenu.objects.filter(menu_id=7).values()
    oito = SubMenu.objects.filter(menu_id=8).values()
    nove = SubMenu.objects.filter(menu_id=9).values()
    dez = SubMenu.objects.filter(menu_id=10).values()
    onze = SubMenu.objects.filter(menu_id=11).values()
    doze = SubMenu.objects.filter(menu_id=12).values()
    treze = SubMenu.objects.filter(menu_id=13).values()
    quatorze = SubMenu.objects.filter(menu_id=14).values()
    quinze = SubMenu.objects.filter(menu_id=15).values()
    dezesseis = SubMenu.objects.filter(menu_id=16).values()
    dezessete = SubMenu.objects.filter(menu_id=17).values()
    dezoito = SubMenu.objects.filter(menu_id=18).values()
    dezenove = SubMenu.objects.filter(menu_id=19).values()
    vinte = SubMenu.objects.filter(menu_id=20).values()


    return render(request, 'core/navbar_novo_layout_integrado.html', { 
        'menus': menus,
        'um': um,
        'dois': dois,
        'tres': tres,
        'quatro': quatro,
        'cinco': cinco,
        'seis': seis,
        'sete': sete,
        'oito': oito,
        'nove': nove,
        'dez': dez,
        'onze': onze, 	
        'doze': doze,	
        'treze': treze,	
        'quatorze': quatorze,
        'quinze': quinze,
        'dezesseis': dezesseis,
        'dezessete': dezessete,
        'dezoito': dezoito,
        'dezenove': dezenove, 
        'vinte': vinte,
    
    })


# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)

#         if form.is_valid():
#             form.save()

#             return redirect('/login/')
#     else:
#         form = SignupForm()

#     return render(request, 'core/signup.html', {
#         'form': form
#     })


def logado(request):
    menus = Menu.objects.all()

    return render(request, 'core/logado.html', { 
        'menus': menus,
    })

# def usuario(request):
#     if str(request.method) == 'POST':
#         form = UsuarioModelForm(request.POST, request.FILES)
#         if form.is_valid():
#             prod = form.save(commit=True)
#             # print(f'DRT:  {prod.drt}')
#             # print(f'Nome:  {prod.nome}')
#             # print(f'Perfil:  {prod.perfil_acesso}')
#             messages.success(request, 'Usuário salvo com sucesso')
#             form = UsuarioModelForm()
#         else:
#             messages.error(request, "Erro ao salvar")
#     else:
#         form = UsuarioModelForm()
#     context = {
#         'form': form
#     }      
#     return render(request, 'core/usuario.html', context)

def loginform(request):
    usuarios = Usuario.objects.all()
    forms = UsuarioModelForm(request.POST, request.FILES)
    #print(usuarios)
    # prod = form.save(commit=False)
    # print(f'DRT:  {usuarios.drt}')
    # print(f'Nome:  {usuarios.nome}')
    # print(f'Perfil:  {usuarios.perfil_acesso}')
    messages.success(request, 'Usuários exibidos com sucesso')
    #form = UsuarioModelForm()
    context = {
        'forms': forms,
        'usuarios': usuarios,
    }      
    return render(request, 'core/loginform.html', context)


# @login_required
# def edit(request, pk):
#     # id =1
#     form = UsuarioModelForm(request.POST, request.FILES)
#     usuario = Usuario.objects.filter(id=pk).values
#     if form.is_valid():
#         prod = form.save(commit=False)
#         # print(f'DRT:  {prod.drt}')
#         # print(f'Nome:  {prod.nome}')
#         # print(f'Perfil:  {prod.perfil_acesso}')
#         messages.success(request, 'Usuário salvo com sucesso')
#         # form = UsuarioModelForm()
#     else:
#         messages.error(request, "Erro ao salvar")
#     context = {
#         'form': form,
#         'usuario': usuario,
#     }      
#     return render(request, 'core/editar.html', context)

# def salvar(request):
#     if request.method == 'POST':
#         form = UsuarioModelForm2(request.POST)

#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Usuário salvo com sucesso')
#             return redirect('/login/')
#     else:
#         messages.error(request, "Erro ao salvar")
#         form = UsuarioModelForm2()

#     return render(request, 'core/signup.html', {
#         'form': form
#     })

