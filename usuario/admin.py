from django.contrib import admin
from .models import GrupoAcesso, Usuario

class ModelAdminGrupoAcesso(admin.ModelAdmin):
    model = GrupoAcesso
    list_display_links = ['grupo_acesso', 'nome_grupo']
    list_display = ['id', 'grupo_acesso', 'nome_grupo']

class ModelAdminUsuario(admin.ModelAdmin):
    model = Usuario
    list_display_links = ['drt', 'nome']
    list_display = ['id', 'drt', 'nome', 'cargo', 'perfil_acesso', 'senha']

admin.site.register(Usuario, ModelAdminUsuario)
admin.site.register(GrupoAcesso, ModelAdminGrupoAcesso)

