from django.contrib import admin
from .models import Post

"""Registrar os objetos dentro do site de administração do Django acessado via /admin """
admin.site.register(Post)

