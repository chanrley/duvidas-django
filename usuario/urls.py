from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from usuario.views import userdata, importar

app_name = 'usuario'

urlpatterns = [
    path('list/', views.UsuarioList.as_view(), name='list'),
    path('create/', views.UsuarioCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.UsuarioUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.UsuarioDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.UsuarioDelete.as_view(), name='delete'),
    path('userdata/', views.userdata, name='userdata'),
    path('importar/', views.importar, name='importar'),
    path('userdata/', views.userdata, name='userdata'),
    path('carregar_usuarios/', views.carregar_usuarios, name='carregar_usuarios'),
    
]
