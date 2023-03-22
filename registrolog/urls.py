from django.contrib.auth import views as auth_views
from django.urls import path
from core.forms import LoginForm
from . import views


app_name = 'registrolog'

urlpatterns = [
    
     path('registrolog/', views.index, name='index'),
    
]
