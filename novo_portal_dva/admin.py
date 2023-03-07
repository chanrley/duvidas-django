from django.contrib import admin

from .models import Menu, SubMenu

admin.site.register(Menu)

class ModelAdminSubMenu(admin.ModelAdmin):
    model = SubMenu
    list_display_links = ['nome']
    list_display = ['nome', 'menu', 'menu_id']
    

admin.site.register(SubMenu, ModelAdminSubMenu)

