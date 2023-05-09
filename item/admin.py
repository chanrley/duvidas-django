from django.contrib import admin
from .models import Category, Item, Post

"""Registrar os objetos dentro do site de administração do Django acessado via /admin """
admin.site.register(Category)


class OrderItem(admin.ModelAdmin):
    """Isso é um objeto relacionado a publicação que extende o modelo Item """
    model = Item
    """Campos que serão exibidos"""
    list_display = ['category', 'name', 'description', 'description_with_photo', 'price', 'is_published', 'image', 'created_at']
    """Campos editáveis"""
    list_editable = ['name', 'description', 'price', 'image', 'is_published']
    """Campos somente leitura"""
    readonly_fields = ['created_at']

"""Registrar os objetos dentro do site de administração do Django acessado via /admin """
admin.site.register(Item, OrderItem)

"""Registrar os objetos dentro do site de administração do Django acessado via /admin """
admin.site.register(Post)