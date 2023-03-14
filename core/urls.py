from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm, LogadoForm
from core.views import nova_url, navbar_novo_layout, logado


app_name = 'core'

urlpatterns = [
    path('', views.navbar, name='navbar'),
    path('master/', views.master, name='master'),
    path('navbar/', views.navbar, name='navbar'),
    path('navbar_novo_layout/', views.navbar_novo_layout, name='navbar_novo_layout'),
    path('nova_url/', views.nova_url, name='nova_url'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logado/', views.logado, name='logado'),
    
]
