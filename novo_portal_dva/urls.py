from django.contrib.auth import views as auth_views
from django.urls import path
from core.forms import LoginForm
from . import views

app_name = 'novo_portal_dva'

urlpatterns = [
    
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('novo_portal_dva/', 'index.html', name='index'),
    
]
