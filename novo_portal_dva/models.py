from django.db import models
from usuario.models import Usuario

class Menu(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        ordering = ('nome',)
        verbose_name_plural = 'Menus'
    
    def __str__(self):
        return f'{self.nome}'


class SubMenu(models.Model):
    nome = models.CharField(max_length=255)
    menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('nome', 'menu',)
        verbose_name_plural = 'SubMenus'

    def __str__(self):
        return f"{self.nome} - {self.menu}"

class AcessoAoMenu(models.Model):
    fk_menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE)
    fk_user = models.ForeignKey(to=Usuario, on_delete=models.CASCADE)
    menu_accessed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.fk_menu} - {self.fk_user}"

# class GrupoAcesso(models.Model):
#     grupo_acesso = models.IntegerField()
#     nome_grupo = models.CharField(max_length=100)
    
#     class Meta:
#         ordering = ('nome_grupo',)
#         verbose_name_plural = 'Grupos de acesso'
# #usuario_id = models.ForeignKey(to=Usuario, on_delete=models.CASCADE)
#     def __str__(self):
#         return f"{self.grupo_acesso} - {self.nome_grupo}"


# class Usuario(models.Model):
#     drt = models.CharField(max_length=11)
#     nome = models.CharField(max_length=100)
#     cargo = models.CharField(max_length=100)
#     perfil_acesso = models.ForeignKey(to=GrupoAcesso, on_delete=models.CASCADE)
#     class Meta:
#         ordering = ('nome',)
#         verbose_name_plural = 'Usuários'
#     def __str__(self):
#         return f"{self.nome} - {self.perfil_acesso}"

class Login(models.Model):
    drt = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    perfil_acesso = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('nome',)
        verbose_name_plural = 'Logins'
    def __str__(self):
        return f"{self.drt} - {self.nome}"


class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "cities"

    def __str__(self):
        return self.name
    
