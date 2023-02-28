from django.db import models

class Menu(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        ordering = ('id', 'nome',)
        verbose_name_plural = 'Menus'
    
    def __str__(self):
        return f'{self.nome}'


class SubMenu(models.Model):
    nome = models.CharField(max_length=255)
    menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('menu',)
        verbose_name_plural = 'SubMenus'

    def __str__(self):
        return f"{self.nome} - {self.menu}"

