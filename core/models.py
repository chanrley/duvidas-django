from django.db import models

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
