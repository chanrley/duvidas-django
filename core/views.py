from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from item.models import Category, Item
# from .forms import SignupForm, LogadoForm, LoginForm, UsuarioModelForm, LoginModelForm, UsuarioModelForm2
from django.db import models
from novo_portal_dva.models import models, Menu, SubMenu
# from core.models import Usuario
from django.contrib import messages
from usuario.models import Usuario, GrupoAcessoDetalhe, GrupoAcesso
from core.forms import UsuarioModelForm, DrtModelForm
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from novo_portal_dva.models import City
import logging 
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from item.models import Item
from django.views.generic import DetailView
from item.forms import ItemForm
from django.contrib.auth.models import User
import tkinter
from tkinter import messagebox
from novo_portal_dva.models import AcessoAoMenu, SubMenu, SubMenu3
from django.http import QueryDict



""" Linha que instancia o db_logger para registrar todo o acesso do usuário ao sistema. Deve-se colocar esse objeto em todos os arquivos onde desejar gravar os logs """
db_logger = logging.getLogger('db')

###########################
#Como gravar logs no banco#
###########################
""" Gravar log de info:"""
#db_logger.info('info message XPTO')
""" Gravar log de warning:"""
#db_logger.warning('warning message XPTO')
""" Existem as opções a seguir:
notset, info, warning, debug, error, fatal

"""


def index(request):
    """Função inicial do projeto, porém foi descontinuada"""
    menus = Menu.objects.all()
    submenus = SubMenu.objects.all()

    # return render(request, 'core/index.html', {
    return render(request, 'core/index-portal.html', {
        'menus': menus,
        'submenus': submenus,
    })

def contact(request):
    """Uma das Classes iniciais do projeto, porém foi descontinuada"""
    return render(request, 'core/contact.html')

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)

#         if form.is_valid():
#             form.save()

#             return redirect('/login/')
#     else:
#         form = SignupForm()

#     return render(request, 'core/signup.html', {
#         'form': form
#     })

def nova_url(request):
    """Uma das funções iniciais do projeto, porém foi descontinuada"""
    categories = Category.objects.all()
    return render(request, 'core/nova_url.html', {
        'categories': categories
    })

def master(request):
    """Uma das funções iniciais do projeto, porém foi descontinuada"""
    categories = Category.objects.all()
    return render(request, 'core/master.html', {
        'categories': categories
    })

def navbar(request):
    """Popular navbar com dados do banco de dados, porém foi descontinuada"""
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
    """Popula navbar no novo layout nos padrões do CSF(Carrefour Soluções Financeiras)"""
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
    """Navbar integrada com frontend e backend"""
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

    
    #db_logger.info('info message XPTO')
    #db_logger.warning('warning message XPTO')

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


# def clicar_menu(request):
#     db_logger.warning('menu clicado XPTO')
    
def loggin(request):
    """Função para 'logar' no sistema somente com DRT válido
    Atualmente para efeito de testes existem os seguintes usuários já testados e validados:
    11111111111 = User adm do sistema, tem acesso a tudo, inclusive publicações
    22222222222 = User sem acesso a menus, nem publicações
    33333333333 = User sem acesso a menus, porém com acesso a publicações
    44444444444 = Usuário do SAC, tem acesso a metade dos menus
    55555555555 = Usuário do Atendimento, tem acesso a outra metade dos menus
    """
    # try:

    # db_logger.NotSet(f'Log NotSet exemplo')
    # db_logger.debug(f'Log debug exemplo')
    # db_logger.error(f'Log error exemplo')
    # db_logger.fatal(f'Log fatal exemplo')

    if request.method == "GET":
        return render(request, 'core/loggin.html')
    else:

        print('Entrei no else')
        print(str(request.POST.get('username')))

        username = str(request.POST.get('username'))
        # if username:    
        senha = Usuario.objects.filter(drt=username)
        #user = Usuario.objects.values_list('nome').filter(drt=username)
        user = Usuario.objects.get(drt=username)
        
        
        # ver se coloco um if aqui


        user_grupo_acesso = user.perfil_acesso

        # print(f'Usuário: {user}')

        # perfil_acesso = Usuario.objects.get(drt=username)
        # perfil = models.Usuario.objects.filter(drt__in=perfil_acesso)
        # print(f"perfil: {perfil_acesso}")

        # grupo_acesso = GrupoAcessoDetalhe.objects.values_list('fk_perfil_acesso').filter(fk_perfil_acesso=1)
        grupo_acesso = GrupoAcessoDetalhe.objects.values_list('fk_perfil_acesso').filter(fk_perfil_acesso=user_grupo_acesso)
        
        
        print(f"grupo: {grupo_acesso}")
        print(f"User: {user}")
        print(f"User id: {user.pk}")
        print(f"User nome: {user.nome}")
        print(f"Username: {username}")
        print(f"User perfil: {user.perfil_acesso}")
        
            
        ##################
        #Trabalhando aqui#
        ##################
        # id = user.id
        # id =1
        
        # fk_users = AcessoAoMenu.objects.get(pk=id)
        # fk_users = AcessoAoMenu.objects.values_list('fk_user', flat=True).filter(pk=user.pk) #funciona
        # fk_users = AcessoAoMenu.objects.values_list('fk_user').filter(fk_user=user.nome)
    
        perfil = Usuario.objects.values_list('perfil_acesso').filter(drt=username)
        
        # print(f"Perfil: {perfil}")
        
        if (1,) in perfil:
            perfil_user = 1
        elif(2,) in perfil:
            perfil_user = 2  
        elif(3,) in perfil:
            perfil_user = 3
        elif(4,) in perfil:
            print('entrei no elif 4')
            perfil_user = 4
        elif(5,) in perfil:
            perfil_user = 5
        else:
            perfil_user = 2
    
        # print(f"perfil_user: {perfil_user}")
    
        fk_users = AcessoAoMenu.objects.values_list('fk_user').filter(id=perfil_user)
        # print(f"fk_users: {fk_users}")
        
        fk_menus = AcessoAoMenu.objects.values_list('fk_user', 'fk_menu', 'menu_accessed').filter(id=perfil_user)
        # print(f"fk_menus: {fk_menus}")
        
        menu_filtrado = Menu.objects.get(id=perfil_user)
        # print(f"menu_filtrado: {menu_filtrado}")
        
        user_pk = user.pk

        usuario_filtrado = Usuario.objects.get(id=user_pk)
        # print(f"usuario_filtrado: {usuario_filtrado}")
        
        # registro = AcessoAoMenu(fk_menu=menu_filtrado, fk_user=usuario_filtrado, menu_accessed=True)
        # registro.save()
        # print(f"Registro: {registro}")
        menu_accessed = True
        
        
        clicar_menu(request, menu_filtrado, usuario_filtrado, menu_accessed, perfil_user, user_pk)


        # print(f"Antes do IF:")
        # print(f"grupo_acesso: {grupo_acesso}")
        # print(f"user.perfil_acesso: {user.perfil_acesso}")
        
        ##################
        #Trabalhando aqui#
        ##################

        ### se for do grupo ADM ou Publicador pode ver o menu de publicações
        if (1,) in grupo_acesso or (3, ) in grupo_acesso:
            ga = True
        else:
            ga = False

        # ga = GrupoAcesso.objects.filter(grupo_acesso=user.perfil_acesso)
        # gap = ga.publicador

        # print(f"Grupo Acesso: {ga}")
        # print(f"Grupo Acesso Publi: {gap}")
        usuario = user.nome

        if (1,) in grupo_acesso:
            # print('Entrei no if')

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
            contexto = {
                    'ga': ga,
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
                    'user': user,
                    'menu_filtrado': menu_filtrado,
                    'usuario_filtrado': usuario_filtrado, 
                    'menu_accessed': menu_accessed, 
                    'perfil_user': perfil_user,
                    'user_pk': user_pk,
                    'usuario': usuario,
            }

        elif (2,) in grupo_acesso:
            
            print(f'grupo_acesso no elif 2: {grupo_acesso}')

            menus = Menu.objects.filter(grupo_acesso=2)
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

            user.perfil_acesso
            contexto = {
                    'ga': ga,
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
                    'user': user,
                    'menu_filtrado': menu_filtrado,
                    'usuario_filtrado': usuario_filtrado, 
                    'menu_accessed': menu_accessed, 
                    'perfil_user': perfil_user,
                    'user_pk': user_pk,

            }
        
        elif (3,) in grupo_acesso:
            menus = Menu.objects.filter(grupo_acesso=3)
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

            

            user.perfil_acesso
            contexto = {
                    'ga': ga,
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
                    'user': user,
                    'menu_filtrado': menu_filtrado,
                    'usuario_filtrado': usuario_filtrado, 
                    'menu_accessed': menu_accessed, 
                    'perfil_user': perfil_user,
                    'user_pk': user_pk,
            }
        
        elif (4,) in grupo_acesso: # ver aqui 26/04/23 15:44
            print(f"elif 4")
            menus = Menu.objects.all().filter(grupo_acesso=4)
            
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

            user.perfil_acesso
            contexto = {
                    'ga': ga,
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
                    'user': user,
                    'menu_filtrado': menu_filtrado,
                    'usuario_filtrado': usuario_filtrado, 
                    'menu_accessed': menu_accessed, 
                    'perfil_user': perfil_user,
                    'user_pk': user_pk,

            }
        
        elif (5,) in grupo_acesso:
            menus = Menu.objects.all().filter(grupo_acesso=5)
            
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

            user.perfil_acesso
            contexto = {
                    'ga': ga,
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
                    'user': user,
                    'menu_filtrado': menu_filtrado,
                    'usuario_filtrado': usuario_filtrado, 
                    'menu_accessed': menu_accessed, 
                    'perfil_user': perfil_user,
                    'user_pk': user_pk,

            }
        
        
        else:
            return redirect(request, 'core/loggin.html')
            # print('Entrei no else')
        # print(type(username))
        # print(username)
        # print(type(senha))
        # print(senha)

        # drt = username
        # user = authenticate(username=username, password=senha)
        # print(drt)
    
    
    # print(f"Depois do IF:")
        
        for username in senha:
            # login_django(request, user)
            # print("Entrou no for")        
            # print(grupo_acesso)
            
            #Mensagem de sucesso
            # root = tkinter.Tk()
            # root.withdraw()
            # # Message Box
            # messagebox.showinfo("Informação", "Usuário logado com sucesso")
            """Gravando entrada do usuário no banco de dados"""
            db_logger.info(f'User {username} logado')
            return render(request, 'core/index-portal.html', contexto)
        
            # return HttpResponse('Autenticado')     
        else:
            return HttpResponse("DRT não cadastrado. Contate o Administrador.")
    # except:
        # return HttpResponse("<h2>DRT não cadastrado. Contate o Administrador.</h2>")
    # else:
        # return HttpResponse("DRT não cadastrado. Contate o Administrador.")
    
def clicar_menu(request, menu_filtrado, usuario_filtrado, menu_accessed, perfil_user, user_pk):    
    
    #print(f"clicar_menu")

    menu_filtrado = Menu.objects.get(id=perfil_user)
    # print(f"menu_filtrado: {menu_filtrado}")

    usuario_filtrado = Usuario.objects.get(id=user_pk)
    # print(f"usuario_filtrado: {usuario_filtrado}")
    
    registro = AcessoAoMenu(fk_menu=menu_filtrado, fk_user=usuario_filtrado, menu_accessed=menu_accessed)
    registro.save()

    # print(f"Registro: {registro}")

    return (request, f'Registro inserido')

def clicar_menu2(request):
    teste = request.GET['menu_filtrado']
    print(f'Var teste: {teste}')
    

    menu_filtrado = request.menu_filtrado
    usuario_filtrado = request.usuario_filtrado
    menu_accessed = request.menu_accessed
    perfil_user = request.perfil_user
    user_pk = request.user_pk

    menu_filtrado = Menu.objects.get(id=perfil_user)
    print(f"menu_filtrado: {menu_filtrado}")

    usuario_filtrado = Usuario.objects.get(id=user_pk)
    print(f"usuario_filtrado: {usuario_filtrado}")
    
    registro = AcessoAoMenu(fk_menu=menu_filtrado, fk_user=usuario_filtrado, menu_accessed=menu_accessed)
    registro.save()
    print(f"Registro: {registro}")
    return (f'Registro inserido')

def logado(request):
    """Renderiza a tela logado.html, porém foi descontinuado"""
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
    """Descontinuado"""
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

def entrar(request):
    """Descontinuado"""
    if str(request.method)=='POST':
        form = DrtModelForm(request.POST)
        # print(form)
        context = {
            'form': form
        }
        return render(request, 'core/entrar.html', context)
    else:
        return render(request, 'core/acesso_negado.html') #criar página
        # form = DrtModelForm()
    
   
 
    # return render(request, 'core/index-portal.html')


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



class HomePageView(TemplateView):
    """Classe que renderiza a tela de pesquisa"""
    template_name = 'core/pesquisa.html'

class SearchResultsView(ListView):
    """Classe que pesquisa um objeto no banco"""
    model = Menu
    template_name = 'core/search_results.html'
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Menu.objects.filter(
            Q(nome__icontains=query) | Q(nome__icontains=query)
        )
        return object_list

class NavbarView(TemplateView):
    """Classe que renderiza a navbar no novo layout de acordo com o frontend padrão da DVA"""
    template_name = 'core/navbar_novo_layout_integrado.html'


class ProcuraMenuView(ListView):
    """Classe que procura um menu"""
    model = Menu
    template_name = 'core/navbar_novo_layout_integrado_filtrado.html'
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Menu.objects.filter(
            Q(nome__icontains=query) | Q(nome__icontains=query)
        )
        return object_list
    
class ProcuraSubMenuView(ListView):
    """Classe que procura um Submenu"""
    model = SubMenu
    template_name = 'core/navbar_novo_layout_integrado_filtrado2.html'
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = SubMenu.objects.filter(
            Q(nome__icontains=query) | Q(nome__icontains=query)
        )
        return object_list
    
# class IndexPortalView(TemplateView):
#     template_name = 'core/index-portal.html'
#     menus = Menu.objects.all()
#     object_list = menus

#     def get_queryset(self):
#         # query = self.request.GET.get("q")
#         object_list = Menu.objects.all()
#         print(object_list)
#         return object_list

# @login_required
def index_portal(request):
    """Função que renderiza o index-portal.html"""
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
    
    # user = request.GET.get('username')
    # print(user)
    # db_logger.info(f'Usuário: {user} entrou')
    # db_logger.warning('warning message XPTO')

    return render(request, 'core/index-portal.html', { 
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


def conteudo(request):
    """Função que renderiza a pagina de conteudo.html"""
    # if request.method == "GET":
    #     return render(request, 'core/loggin.html')
    # else:
    # print('Entrei no else')
    # username = str(request.POST.get('username'))
    # senha = Usuario.objects.filter(drt=username)
    # user = Usuario.objects.values_list('nome').filter(drt=username)

    # print(user)
    
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
    # print(type(username))
    # print(username)
    # print(type(senha))
    # print(senha)

    # drt = username
    # user = authenticate(username=username, password=senha)
    # print(drt)
    # for username in senha:
    #     # login_django(request, user)
    #     # print("Entrou no for")        
    #     print(senha)
    
    return render(request, 'core/conteudo.html', {
            
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


def testar(request):
    """Função de testes"""
    return render(request, 'core/testar.html')

def crud_lista(request , user):
    """Função que renderiza o arquivo crud_lista.html"""
    # , perfil_user
    # print(vars(request))

    print(f'crud_lista - usuario {user}')

    usuario = user
    print(f'user: {usuario}')
    

    item = Item.objects.all().filter(is_published=True)
    contexto = {
        'item': item,
        'usuario': usuario,
    }
    return render(request, 'core/crud_lista.html', contexto)

def crud_lista2(request):
    """Função que renderiza o arquivo crud_lista2.html"""
    # , perfil_user
    # usr = request.GET['usuario']
    # print(f'Usuário no crud_lista2: {usr}')

    item = Item.objects.all().filter(is_published=True)
    contexto = {
        'item': item,
    }
    return render(request, 'core/crud_lista2.html', contexto)

def canais_especiais(request):
    """Função que renderiza o arquivo canais_especiais.html"""
    item = Item.objects.all().filter(is_published=True)
    contexto = {
        'item': item,
    }
    return render(request, 'core/canais_especiais.html', contexto)

def aplicativos(request, usuario):
    """Função que renderiza o arquivo aplicativos.html"""
    # , perfil_user
    # item = Item.objects.all().filter(is_published=True)
    # contexto = {
    #     'item': item,
    # }

    print(f"Usuario: {usuario}")
    return render(request, 'core/aplicativos.html', {'usuario': usuario})


def busca(request):
    """Função que renderiza o arquivo busca.html"""
    item = Item.objects.all()
    contexto = {
        'item': item,
    }
    return render(request, 'core/busca.html', contexto)

def visualizar(request):
    """Função que printa no terminal uma mensagem"""
    print("Visualizar")


class ItemDetail(DetailView):
    """Classe que busca todos os Itens"""
    queryset = Item.objects.all()


def remove_publicacao(request, id):
    """Função que remove um Item e renderiza o template 'crud_lista.html'"""
    #print("entrei no remove") # não entra
    
    item = Item.objects.get(id=id)
    item.delete()

    item = Item.objects.all()
    contexto = {
        'item': item
    }
    return render(request, 'core/crud_lista.html', contexto)

# def remove_publicacao2(request, id):
#     print("entrei no remove2")

#     items = Item.objects.get(id=id)
#     items.delete()

#     items = Item.objects.all()
#     contexto = {
#         'items': items
#     }
#     return render(request, 'core/crud_lista.html', contexto)

def item_delete(request, id):
    """Deleta um Item"""
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('core:crud_lista')

def item_delete2(request, id):
    """Marca um Item como não publicado em vez de deletar"""
    perfil_user = request.POST.get('1')

    # print(f"Perfil_user: {perfil_user}")

    item = get_object_or_404(Item, pk=id)
    # print(f"user: {item.usuario}")
    # print(vars(item))
    
    item.is_published = False
    item.save()
    
    # item.delete()
    return redirect('core:crud_lista2')


def item_update(request, id):
    """Atualiza um item e renderiza a tela 'crud_lista.html' caso seja método POST renderiza a página 'editar.html' caso seja método GET renderiza a página 'editar.html' """
    # print("pronto")
    # user =  
    # u = request.GET['usuario']
    # print(f'Usuário: {u}')

    item = Item.objects.all().filter(is_published=True)

    items = get_object_or_404(Item, pk=id)
    
    form = ItemForm(instance=items)
    disabled = "disabled"
    # usr = ""

    if(request.method == 'POST'):
        form = ItemForm(request.POST, instance=items)	
        if(form.is_valid()):
            # print("Form válido")
            #
            # print(vars(request.POST['usr']))
            usr  = get_object_or_404(Item, pk=id)
            usuario = usr.usuario

            print('Entrei no post')
            # usuario = request.POST.get('usuario', '')
            print(f'Usuario: {usuario}')
            # print(vars(request))


            # items.usuario = form.cleaned_data['usuario']
            # items.usuario = form.cleaned_data['usuario']
            items.category = form.cleaned_data['category']
            items.name = form.cleaned_data['name']
            items.description = form.cleaned_data['description']
            items.description_with_photo = form.cleaned_data['description_with_photo']
            items.is_published = form.cleaned_data['is_published']
            items.created_by = form.cleaned_data['created_by']
            # items.created_at = form.cleaned_data['created_at']
            items = form.save(commit=True)
            items.save()
            ####
            # item = Item.objects.all()
            # items = get_object_or_404(Item, pk=id)
            ###
            
            return render(request, 'core/crud_lista.html', {'items': items, 'item': item})
        
        else:
            return render(request, 'core/editar.html', {'form': form, 'items' : items})

    elif(request.method == 'GET'):
        # print(vars(request))
        print('entrei no GET')
        usuario = request.GET.get('usuario', '')
        print(f'Usuario: {usuario}')

        return render(request, 'core/editar.html', {'form': form, 'items' : items, 'disabled': disabled, 'usuario': usuario })
    

def item_visualizar(request, id):
    """Visualiza um item e renderiza o 'item_visualizar.html' """
    # #print("Entrei no visualizar")
    # ver_item = get_object_or_404(Item, pk=id)
    # form = ItemForm(instance=ver_item)
    # #print(vars(ver_item)) #semelhante ao var_dump(variavel) no PHP pois printa o objeto inteiro
    # #print(vars(form))
    
    # if(request.method == 'GET'):
    #     print("Entrei no IF")
    #     return redirect(request, 'core/item_visualizar.html', {'ver_item': ver_item})
    # else:
    #     return render(request, 'core/crud_lista.html', {'form': form, 'ver_item' : ver_item})
    item = get_object_or_404(Item, pk=id)
    
    usuario = request.GET.get('usuario')
    db_logger.info(f'Item {id } visualizado pelo usuário: {usuario}')
    print(f'Usuário {usuario}')
    # print(vars(request))


    return render(request, 'core/item_visualizar.html', {'item': item, 'usuario': usuario})

def item_create(request):
    """Cria um item / publicação e renderiza o template 'item_create.html"""
    # user = authenticate(drt=11111111111)
    # print(user)

    if request.method == 'GET':
        form = ItemForm(request.GET)
        if form.is_valid():
#            print("form valido")
            item = form.save(commit=True)
            db_logger.info(f'Publicação "{item.name}" criada ')
            # print("cheguei no redirect")
            return redirect('../crud_lista2', pk=item.pk)
            # return redirect('../crud_lista', 1)
            
    else:
        form = ItemForm()
    return render(request, 'core/item_create.html', {'form': form})

def item_create2(request, usuario):
    """Nova função que cria um item recebendo o parametro usuario  que Cria um item / publicação e renderiza o template 'crud_lista2.html recebendo o usuário como parâmetro """
    # user = authenticate(drt=11111111111)
    # print(user)

    if request.method == 'GET':
        form = ItemForm(request.GET)
        if form.is_valid():
#            print("form valido")
            item = form.save(commit=True)
            db_logger.info(f'Publicação "{item.name}" criada ')
            # print("cheguei no redirect")
            contexto = {'usuario': usuario}
            # return redirect('../crud_lista2', pk=item.pk) #funcionando
            print(f'Usuário no get: {usuario}')
            return redirect('../crud_lista2', contexto)
            
            # return redirect('../crud_lista', 1)
            
    else:
        form = ItemForm()
    return render(request, 'core/item_create.html', {'form': form, 'usuario': usuario})

def item_create3(request, usuario):
    """Tentativa de criar um objeto no submenu3 dinamicamente"""
    # user = authenticate(drt=11111111111)
    # print(user)

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
#            print("form valido")
            item = form.save(commit=True)
            db_logger.info(f'Publicação "{item.name}" criada ')
            # print("cheguei no redirect")
            contexto = {'usuario': usuario}
            usr = usuario


            # return redirect('../crud_lista2', pk=item.pk) #funcionando
            print(f'Usuário no post: {usuario}')
            # print(vars(usuario))

            print(f'grupo_acesso: {item.grupo_acesso}')
            print(f'Item pk: {item.pk}')
            print(f'nome submenu3: {item.name}')
            print(f'Item menu: {item.menu}')
            print(f'Item submenu: {item.submenu}')
            
            i_id = item.grupo_acesso 
            
            print(f'i_id: {i_id}')

            i_id_str = str(i_id)
            i_id_str = i_id_str.split(" ")

            print(f'i_id split: {i_id_str}')

            gr_acesso = i_id_str[0]
            print(f'gr_acesso: {gr_acesso}')


            #criar_submenu3
            #criar_submenu3(item.name, item.menu, item.submenu) #funcionando
            # description_with_photo, created_at, created_by
            print(f'antes de criar submenu3')
            criar_submenu3(item.name, item.menu, item.submenu, item.description_with_photo, item.created_at, str(item.created_by))
            print(f'depois de criar submenu3')

            print('description_with_photo:')
            print(item.description_with_photo)
            
            created_by = item.created_by
            print('created_by:')
            print(f'{created_by}')

            description_with_photo = item.description_with_photo
            
            created_at = item.created_at
            print('created_at:')
            print(f'{created_at}')

            item = Item.objects.filter(is_published=True, grupo_acesso = gr_acesso).values()
            # item = get_object_or_404(Item, is_published=True, grupo_acesso = 1).first()


            # até aqui ok, agora vem a outra parte
            # print('Item:')
            # print(vars(item))

            # grupoacesso = item.grupo_acesso.split(" ")
            # print(f"gr acesso: {grupoacesso}")


            men = Menu.objects.filter(grupo_acesso=gr_acesso)
            # print('Menu:')
            # print(vars(men))
            #testando
            sub = SubMenu.objects.filter(grupo_acesso=gr_acesso)
            
            # print('SubMenu:')
            # print(vars(sub))
            
            sub3 = SubMenu3.objects.filter(menu_id=gr_acesso)
            # print('SubMenu3:')
            # print(vars(sub3))


            # sub = 1

            

            # submenu3 = SubMenu3.objects.filter(menu=)
            # menu = Menu.objects.all().filter(is_published=True) #ver para filtrar

            # print('Item:')
            # print(vars(item))

            # return redirect('../crud_lista2', {'usuario': usuario, 'usr': usr})
            return render(request, 'core/crud_lista2.html', {'form': form, 'usuario': usuario, 'item': item, \
                                                            'men': men, 'sub': sub, 'sub3': sub3, \
                                                            'description_with_photo': description_with_photo, \
                                                            'created_by': created_by, 'created_at': created_at})
        
        
        
            
            # return redirect('../crud_lista', 1)
            
    else:
        form = ItemForm()
    return render(request, 'core/item_create.html', {'form': form, 'usuario': usuario})

def criar_submenu3(nome, menu, submenu, description_with_photo, created_at, created_by):
    # print(vars(request))
    # print(f'nome {nome}')
    # print(f'Menu {menu}')
    # print(f'SubMenu {submenu}')
    print(f'description_with_photo: {description_with_photo}')
    print(f'created_at: {created_at}')
    print(f'created_by: {created_by}')


    submenu = SubMenu3.objects.create(nome=nome, menu=menu, submenu=submenu, \
                                        description_with_photo=description_with_photo, created_at=created_at, \
                                        created_by=created_by)
    submenu.save()




def tabela_de_funcionalidades(request, usuario):
    """Função que renderiza o arquivo tabela_de_funcionalidades.html"""
    # , perfil_user
    # item = Item.objects.all().filter(is_published=True)
    # contexto = {
    #     'item': item,
    # }

    print(f"Usuario: {usuario}")
    return render(request, 'core/tabela_de_funcionalidades.html', {'usuario': usuario})

def pagina_padrao_nao_existe(request, usuario):
    """Função que renderiza o arquivo pagina_padrao_nao_existe.html"""
    # , perfil_user
    # item = Item.objects.all().filter(is_published=True)
    # contexto = {
    #     'item': item,
    # }

    print(f"Usuario: {usuario}")
    return render(request, 'core/pagina_padrao_nao_existe.html', {'usuario': usuario})

def pagina_dinamica(request, nome_pagina):
    """Função que renderiza o arquivo pagina_dinamica.html"""
    try:    
        # , perfil_user
        print(f'nome_pagina: {nome_pagina}')
        # print(vars(request))


        item = Item.objects.all().filter(is_published=True)
        # contexto = {
        #     'item': item,
        # }

        # print(f'Request: {request}')
        # print(vars(request))
        
        print(f'Função dinamica')

        # teste = request.POST['teste']
        # usuario = request.POST['usuario']

        if request.POST['teste']:

            # print(f'teste: {teste}')

            
            description_with_photo = request.POST['description_with_photo']
            print(f'description_with_photo: {description_with_photo}')

            print(f"nome_pagina: {nome_pagina}")

            created_at = request.POST['created_at']
            print(f'created_at: {created_at}')

            created_by = request.POST['created_by']
            print(f'created_by: {created_by}')


            print('caminho normal')
            return render(request, 'core/pagina_dinamica.html', {'nome_pagina': nome_pagina, 'teste': 'teste', 'item': item, \
                                                                'description_with_photo': description_with_photo, \
                                                                'created_at': created_at, 'created_by': created_by})
        else:
            return render(request, 'core/pagina_padrao_nao_existe.html', {'nome_pagina': nome_pagina})

    # except MultiValueDictKeyError as error:
    # except ZeroDivisionError as error:
    except NameError as error:
        db_logger.error('Erro {error} aconteceu')
        print(f'Erro: {error}')
        
    # except UnboundLocalError as error:
    #     db_logger.error('Erro {error} aconteceu')
    #     print(f'Erro: {error}')

    else:
        print('Sem erros')
    # finally:
    #     print("finally")
    #     # if description_with_photo:
    #     return render(request, 'core/pagina_dinamica.html', {'nome_pagina': nome_pagina})                
    #     # else:
            # return HttpResponse("<h2>Página não encontrada</h2>")


