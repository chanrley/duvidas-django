from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import index, detail
from . import views 
from django.conf import settings
from django.conf.urls.static import static

app_name = 'article'

urlpatterns = [
 path('', views.index, name='index'),
#  path('detail/', views.detail, name='detail'),
 path('detail/<int:id>', views.detail, name='detail'),
 path('ckeditor', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#only for development environment, in production using nginx instead

