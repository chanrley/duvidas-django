from django.contrib import admin

from .models import Menu, SubMenu, AcessoAoMenu

admin.site.register(Menu)

class ModelAdminSubMenu(admin.ModelAdmin):
    model = SubMenu
    list_display_links = ['nome']
    list_display = ['nome', 'menu', 'menu_id']

admin.site.register(SubMenu, ModelAdminSubMenu)

admin.site.register(AcessoAoMenu)


# class ModelAdminGrupoAcesso(admin.ModelAdmin):
#     model = GrupoAcesso
#     list_display_links = ['grupo_acesso', 'nome_grupo']
#     list_display = ['id', 'grupo_acesso', 'nome_grupo']

# class ModelAdminUsuario(admin.ModelAdmin):
#     model = Usuario
#     list_display_links = ['drt', 'nome']
#     list_display = ['id', 'drt', 'nome', 'cargo', 'perfil_acesso']

# admin.site.register(Usuario, ModelAdminUsuario)
# admin.site.register(GrupoAcesso, ModelAdminGrupoAcesso)



