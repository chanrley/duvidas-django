from django.db import models

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

# class Usuario(models.Model):
#     drt = models.CharField(max_length=11)
#     nome = models.CharField(max_length=100)
#     cargo = models.CharField(max_length=100)
#     perfil_acesso = models.ForeignKey(to=GrupoAcesso, on_delete=models.CASCADE)
#     class Meta:
#         ordering = ('drt',)
#         verbose_name_plural = 'Usuários'

# class GrupoAcesso(models.Model):
#     usuario_id = models.ForeignKey(to=Usuario, on_delete=models.CASCADE)
#     grupo_acesso = models.IntegerField()
    
#     class Meta:
#         ordering = ('drt',)
#         verbose_name_plural = 'Usuários'
