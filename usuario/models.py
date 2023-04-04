from django.db import models

class GrupoAcesso(models.Model):
    grupo_acesso = models.IntegerField()
    nome_grupo = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('nome_grupo',)
        verbose_name_plural = 'Grupos de acesso'
#usuario_id = models.ForeignKey(to=Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.grupo_acesso} - {self.nome_grupo}"


class Usuario(models.Model):
    drt = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    perfil_acesso = models.ForeignKey(to=GrupoAcesso, on_delete=models.CASCADE)
    senha = models.CharField(max_length=11, default=1)

    class Meta:
        ordering = ('nome',)
        verbose_name_plural = 'Usuários'
    
    def __str__(self):
        return f"{self.nome} - {self.perfil_acesso} - {self.senha}"
    
class GrupoAcessoDetalhe(models.Model):
    fk_perfil_acesso = models.ForeignKey(to=GrupoAcesso, on_delete=models.CASCADE)
    detalhe_acesso = models.IntegerField()
    
    class Meta:
        ordering = ('fk_perfil_acesso',)
        verbose_name_plural = 'Detalhes Grupo de Acesso'
    
    def __str__(self):
        return f"{self.fk_perfil_acesso} - {self.detalhe_acesso}"

