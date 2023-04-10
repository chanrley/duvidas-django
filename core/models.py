from django.db import models
from ckeditor.fields import RichTextField


class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "cities"

    def __str__(self):
        return self.name
    
class Testar(models.Model):
  nome = models.CharField(max_length=255)

  class Meta:
    verbose_name_plural = "testes"
    
  def __str__(self):
    return self.nome

class Post(models.Model):
    title = models.CharField(max_length=255)
    body1 = models.TextField(blank=True, null=True)
    body2 = RichTextField(blank=True, null=True)
