from django.db import models
from ckeditor.fields import RichTextField


class City(models.Model):
    """Classe criada para testar as chaineds dropdowns(tradução livre caixas de listagem encadeadas)"""
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
      """Nome no plural"""
      verbose_name_plural = "cities"

    """Representação textual do objeto"""
    def __str__(self):
        return self.name
    
class Testar(models.Model):
  """Classe para testes """
  nome = models.CharField(max_length=255)

  class Meta:
    """Nome no plural """
    verbose_name_plural = "testes"
  
  """Representação textual do objeto"""
  def __str__(self):
    return self.nome

class Post(models.Model):
    """Classe criada para testar a biblioteca CKEditor """
    title = models.CharField(max_length=255)
    body1 = models.TextField(blank=True, null=True)
    body2 = RichTextField(blank=True, null=True)
