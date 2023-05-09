from django.db import models
# from .models import Setor

class GrupoAcesso(models.Model):
    """Classe que guarda os possíveis perfis de acesso, sendo padrão o número 2 - Usuário Call Center que por padrão não são usuários 'publicadores' """
    grupo_acesso = models.IntegerField(default=2)
    nome_grupo = models.CharField(max_length=100)
    publicador = models.BooleanField(default=False)
    
    class Meta:
        """Ordenação pelo campo a seguir"""
        ordering = ('nome_grupo',)
        """Maneira que 'aparece' no admin(utilizado para plurais principalmente)"""
        verbose_name_plural = 'Grupos de acesso'
    #usuario_id = models.ForeignKey(to=Usuario, on_delete=models.CASCADE)
    """Como exibir o item como string"""
    def __str__(self):
        # return f"{self.grupo_acesso} - {self.nome_grupo}"
        return f"{self.grupo_acesso} - {self.nome_grupo}"


class Usuario(models.Model):
    """Classe relacionada ao usuário do sistema que pode conter no máximo 11 caracteres e por padrão recebe o grupo de acesso 2 - Usuário Call Center """
    drt = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    perfil_acesso = models.ForeignKey(to=GrupoAcesso, on_delete=models.CASCADE, default=2)
    # perfil_acesso = models.CharField(max_length=100)
    senha = models.CharField(max_length=11, default=1)
    # setor = models.ForeignKey(to=Setor, on_delete=models.CASCADE)

    class Meta:
        """Ordenação alfabética pelo campo nome"""
        ordering = ('nome',)
        """Nome no plural"""
        verbose_name_plural = 'Usuários'
        """Nome comum"""
        verbose_name = 'usuario'
    
    """Representação em texto do objeto"""
    def __str__(self):
        return f"{self.nome} - {self.perfil_acesso} - {self.senha}"
        # return f"{self.perfil_acesso}"
    
class GrupoAcessoDetalhe(models.Model):
    """Classe que determina quais grupo de usuários tem acesso a quais menus"""
    fk_perfil_acesso = models.ForeignKey(to=GrupoAcesso, on_delete=models.CASCADE)
    detalhe_acesso = models.IntegerField()
    
    class Meta:
        """Classificação por chave estrangeira fk_perfil de acesso"""
        ordering = ('fk_perfil_acesso',)
        verbose_name_plural = 'Detalhes Grupo de Acesso'
    
    """Representação em texto do objeto"""
    def __str__(self):
        return f"{self.fk_perfil_acesso} - {self.detalhe_acesso}"

