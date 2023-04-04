from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('log/', include('log.urls')),
    path('registrolog/', include('registrolog.urls')),
    path('core/', include('core.urls')),
    path('', include('core.urls')),
    path('usuario/', include('usuario.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
