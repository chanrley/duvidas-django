from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .forms import LoginForm, LogadoForm
from .views import HomePageView, SearchResultsView, NavbarView, ProcuraMenuView, ProcuraSubMenuView, testar, loggin, remove_publicacao

from django.conf import settings
from django.conf.urls.static import static



def test(request):
    pass
    # division = 1 / 0 #EX: 1
    # division = a / 1 #EX: 2


app_name = 'core'

urlpatterns = [
    # path('master/', views.master, name='master'),
    # path('navbar/', views.navbar, name='navbar'),
    # path('navbar_novo_layout/', views.navbar_novo_layout, name='navbar_novo_layout'),
    path('navbar_novo_layout_integrado/', views.navbar_novo_layout_integrado, name='navbar_novo_layout_integrado'),
    # path('navbar_novo_layout_integrado_filtrado/', views.navbar_novo_layout_integrado_filtrado, name='navbar_novo_layout_integrado_filtrado'),
    # path('nova_url/', views.nova_url, name='nova_url'),
    path('contact/', views.contact, name='contact'),
    # path('signup/', views.signup, name='signup'),
    # path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('loggin/<int:id>', views.loggin, name='loggin'),
    path('', views.loggin, name='loggin'),
    path('crud_lista/<str:user>', views.crud_lista, name='crud_lista'),
    
    path('crud_lista2/', views.crud_lista2, name='crud_lista2'),
    path('canais_especiais/', views.canais_especiais, name='canais_especiais'),
    
    #Parei aqui
    path('aplicativos/<str:usuario>', views.aplicativos, name='aplicativos'),


    path('conteudo/', views.conteudo, name='conteudo'),
    path('busca/', views.busca, name='busca'),
    path('visualizar/', views.visualizar, name='visualizar'),
    path('remove_publicacao/<int:id>/', views.remove_publicacao, name='remove_publicacao'),    
    path('deletar/<int:id>/', views.item_delete, name='item_delete'),
    ##############################################
    #Marcar False na publicação em vez de excluir#
    ##############################################
    path('deletar2/<int:id>/', views.item_delete2, name='item_delete2'),

    
    path('item_update/<int:id>/', views.item_update, name='item_update'),
    #######################
    #Criação de publicação#
    #######################
    path('item_create/', views.item_create, name='item_create'),

    #######################
    #Criação de publicação2#
    #######################
    path('item_create2/<str:usuario>', views.item_create2, name='item_create2'),

    ##################
    #Visualizar items#
    ##################
    path('item_visualizar/<int:id>/', views.item_visualizar, name='item_visualizar'),
    
    ##################
    #Clicar menu#
    ##################
    path('clicar_menu/<int:id>/', views.clicar_menu, name='clicar_menu'),
    path('clicar_menu2/', views.clicar_menu2, name='clicar_menu2'),
    
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('detail/<int:pk>/', views.ItemDetail.as_view(), name='detail'),
    # path('', views.loggin, name='loggin'),
    # path('logado/', views.logado, name='logado'),
    # path('usuario/', views.usuario, name='usuario'),
    # path('loginform/', views.loginform, name='loginform'),
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("pesquisa/", HomePageView.as_view(), name="pesquisa"),
    path("index-portal/", views.index_portal, name="index-portal"),
    # path("entrar/", views.entrar, name="entrar"),

    path("navbar_novo_layout_integrado_filtrado/", ProcuraMenuView.as_view(), name="navbar_novo_layout_integrado_filtrado"),
    path("navbar_novo_layout_integrado_filtrado2/", ProcuraSubMenuView.as_view(), name="navbar_novo_layout_integrado_filtrado2"),
    path("busca/", NavbarView.as_view(), name="NavbarView"),
    path('test/', test),
    path('testar/', views.testar, name='testar'),
    path('tabela_de_funcionalidades/<str:usuario>', views.tabela_de_funcionalidades, name='tabela_de_funcionalidades'),
    path('pagina_padrao_nao_existe/<str:usuario>', views.pagina_padrao_nao_existe, name='pagina_padrao_nao_existe'),
    path('pagina_dinamica/<str:nome_pagina>', views.pagina_dinamica, name='pagina_dinamica'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#only for development environment, in production using nginx instead

