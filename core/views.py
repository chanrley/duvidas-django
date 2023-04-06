from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from item.models import Category, Item
# from .forms import SignupForm, LogadoForm, LoginForm, UsuarioModelForm, LoginModelForm, UsuarioModelForm2
from django.db import models
from novo_portal_dva.models import models, Menu, SubMenu
# from core.models import Usuario
from django.contrib import messages
from usuario.models import Usuario, GrupoAcessoDetalhe
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


# db_logger = logging.getLogger('db')
db_logger = logging.getLogger('db')


def index(request):
    menus = Menu.objects.all()
    submenus = SubMenu.objects.all()

    # return render(request, 'core/index.html', {
    return render(request, 'core/index-portal.html', {
        'menus': menus,
        'submenus': submenus,
    })

def contact(request):
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


    db_logger.info('info message XPTO')
    db_logger.warning('warning message XPTO')

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
#    return render(request, 'core/login.html')

    if request.method == "GET":
        return render(request, 'core/loggin.html')
    else:
        # print('Entrei no else')
        username = str(request.POST.get('username'))
        senha = Usuario.objects.filter(drt=username)
        user = Usuario.objects.values_list('nome').filter(drt=username)

        
        
        # perfil_acesso = Usuario.objects.get(drt=username)
        # perfil = models.Usuario.objects.filter(drt__in=perfil_acesso)
        # print(f"perfil: {perfil_acesso}")
        
        grupo_acesso = GrupoAcessoDetalhe.objects.values_list('fk_perfil_acesso').filter(fk_perfil_acesso=2)
        
        print(f"grupo: {grupo_acesso}")
        

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
            }
        elif (2,) in grupo_acesso:
            menus = Menu.objects.all()
            oito = SubMenu.objects.filter(menu_id=8).values()
            contexto = {
                    'menus': menus,
                    'oito': oito,
                    'user': user,
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
        for username in senha:
            # login_django(request, user)
            # print("Entrou no for")        
            print(grupo_acesso)
            return render(request, 'core/index-portal.html', contexto)
        
            # return HttpResponse('Autenticado')     
        else:
            return HttpResponse("User ou senha inválidos")
    
    


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

def entrar(request):
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
    template_name = 'core/pesquisa.html'

class SearchResultsView(ListView):
    model = Menu
    template_name = 'core/search_results.html'
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Menu.objects.filter(
            Q(nome__icontains=query) | Q(nome__icontains=query)
        )
        return object_list

class NavbarView(TemplateView):
    template_name = 'core/navbar_novo_layout_integrado.html'


class ProcuraMenuView(ListView):
    model = Menu
    template_name = 'core/navbar_novo_layout_integrado_filtrado.html'
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Menu.objects.filter(
            Q(nome__icontains=query) | Q(nome__icontains=query)
        )
        return object_list
    
class ProcuraSubMenuView(ListView):
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
    
    db_logger.info('info message XPTO')
    db_logger.warning('warning message XPTO')

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
    return render(request, 'core/testar.html')

def crud_lista(request):
    item = Item.objects.all()
    contexto = {
        'item': item
    }
    return render(request, 'core/crud_lista.html', contexto)

def busca(request):
    item = Item.objects.all()
    contexto = {
        'item': item,
    }
    return render(request, 'core/busca.html', contexto)

def visualizar(request):
    print("Visualizar")


class ItemDetail(DetailView):
    queryset = Item.objects.all()

def remove_publicacao(request, id):
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
    print("pronto")
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('core:crud_lista')

def item_update(request, id):
    print("pronto")
    item = get_object_or_404(Item, pk=id)
    form = ItemForm(instance=item)

    if(request.method == 'POST'):
        form = ItemForm(request.POST, instance=item)	
        if(form.is_valid()):
            print("Form válido")
            
            item.category = form.cleaned_data['category']
            item.name = form.cleaned_data['name']
            item.description = form.cleaned_data['description']
            item.created_by = form.cleaned_data['created_by']
            # item.created_at = form.cleaned_data['created_at']
            item = form.save(commit=True)
            item.save()

            return redirect('core:crud_lista')
        else:
            return render(request, 'core/editar.html', {'form': form, 'item' : item})

    elif(request.method == 'GET'):
        return render(request, 'core/editar.html', {'form': form, 'item' : item})

def item_visualizar(request, id):
    #print("Entrei no visualizar")
    ver_item = get_object_or_404(Item, pk=id)
    form = ItemForm(instance=ver_item)
    #print(vars(ver_item)) #semelhante ao var_dump(variavel) no PHP pois printa o objeto inteiro
    #print(vars(form))
    
    if(request.method == 'GET'):
        print("Entrei no IF")
        return redirect(request, 'core/item_visualizar.html', {'ver_item': ver_item})
    else:
        return render(request, 'core/crud_lista.html', {'form': form, 'ver_item' : ver_item})


def item_create(request):
    if request.method == 'GET':
        form = ItemForm(request.GET)
        if form.is_valid():
#            print("form valido")
            item = form.save(commit=True)
            return redirect('../crud_lista', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'core/item_create.html', {'form': form})
