from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm, LogadoForm

from .views import HomePageView, SearchResultsView, NavbarView, ProcuraMenuView, ProcuraSubMenuView, testar, loggin, remove_publicacao


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
    path('loggin/', views.loggin, name='loggin'),
    path('crud_lista/', views.crud_lista, name='crud_lista'),
    path('conteudo/', views.conteudo, name='conteudo'),
    path('busca/', views.busca, name='busca'),
    path('visualizar/', views.visualizar, name='visualizar'),
    path('remove_publicacao/<int:id>/', views.remove_publicacao, name='remove_publicacao'),
    
    #Trabalhando aqui. Parei aqui    
    path('deletar/<int:id>/', views.item_delete, name='item_delete'),



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

]

