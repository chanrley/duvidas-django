from django.contrib.auth.models import User
from django.db import models

from item.models import Item

class Conversation(models.Model):
    """Classe criada para entendimento do funcionamento do Django"""
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Ordenação decrescente por data de modificação"""
        ordering = ('-modified_at',)
    
class ConversationMessage(models.Model):
    """Classe criada para testes sobre o funcionamento do Django"""
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)