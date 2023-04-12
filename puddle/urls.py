from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from article.views import index
from article import views

urlpatterns = [
    path('log/', include('log.urls')),
    path('registrolog/', include('registrolog.urls')),
    path('core/', include('core.urls')),
    path('', include('core.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    path('usuario/', include('usuario.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),

    path('article/', include('article.urls')),
    
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
