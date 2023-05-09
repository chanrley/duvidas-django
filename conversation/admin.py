from django.contrib import admin

from .models import Conversation, ConversationMessage

"""Registrar os objetos dentro do site de administração do Django acessado via /admin """
admin.site.register(Conversation)
admin.site.register(ConversationMessage)
