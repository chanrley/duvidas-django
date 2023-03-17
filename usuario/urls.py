from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('list/', views.UsuarioList.as_view(), name='list'),
    path('create/', views.UsuarioCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.UsuarioUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.UsuarioDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.UsuarioDelete.as_view(), name='delete'),
]