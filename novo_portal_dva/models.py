from django.db import models
from usuario.models import Usuario, GrupoAcesso
# from item.models import Item

class Menu(models.Model):
    """Objetos do tipo Menu para alimentar a 'sidebar' do projeto"""
    nome = models.CharField(max_length=50)
    grupo_acesso = models.ForeignKey(to=GrupoAcesso, on_delete=models.CASCADE, default=2)
    
    class Meta:
        """Ordenação alfabética por nome e depois grupo de acesso"""
        ordering = ('nome','grupo_acesso',)
        """Nome plural"""
        verbose_name_plural = 'Menus'
    
    """Representação em texto do objeto"""
    def __str__(self):
        return f'{self.nome} - {self.id}'


class SubMenu(models.Model):
    """Objetos do tipo SubMenu para alimentar a lista de Menus na 'sidebar' do projeto"""
    nome = models.CharField(max_length=50)
    menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE)
    grupo_acesso = models.ForeignKey(to=GrupoAcesso, on_delete=models.CASCADE, default=2)
    
    class Meta:
        """Ordenação alfabética por nome, depois menu"""
        ordering = ('nome', 'menu',)
        """Nome no plural"""
        verbose_name_plural = 'SubMenus'
    
    """Representação em texto do objeto"""
    def __str__(self):
        return f"{self.nome} - {self.menu}"

class AcessoAoMenu(models.Model):
    """Objeto criado com o intuito de monitorar/registrar o acesso do usuário a aplicação"""
    fk_menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE)
    fk_user = models.ForeignKey(to=Usuario, on_delete=models.CASCADE)
    menu_accessed = models.BooleanField(default=False)
    
    class Meta:
        """Nome no plural"""
        verbose_name_plural = 'Acesso aos Menus'
    
    """Representação em texto do objeto"""   
    def __str__(self):
        return f"{self.fk_menu} - {self.fk_user} - {self.menu_accessed}"

class SubMenu3(models.Model):
    """Um objeto que representa um subitem de um SubMenu"""
    nome = models.CharField(max_length=50)
    menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE)
    submenu = models.ForeignKey(to=SubMenu, on_delete=models.CASCADE)

    # name = models.ForeignKey(to=Item, on_delete=models.CASCADE, to_field="name")
    # description = models.ForeignKey(to=Item, on_delete=models.CASCADE, to_field="description")

    class Meta:
        """Ordenação alfebética por nome, menu e submenu"""
        ordering = ('nome', 'menu', 'submenu',)
        """Nome no plural"""
        verbose_name_plural = 'SubMenus 3'
    
    """Representação em texto do objeto"""
    def __str__(self):
        return f"{self.nome} - {self.menu}"

# class Setor(models.Model):
#     nome = models.CharField(max_length=50)
#     menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE)
#     submenu = models.ForeignKey(to=SubMenu, on_delete=models.CASCADE)

#     class Meta:
#         ordering = ('nome', 'menu', 'submenu',)
#         verbose_name_plural = 'Setores'

#     def __str__(self):
#         return f"{self.nome} - {self.menu}"



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
    """Classe não utilizada no projeto Novo Portal de Procedimentos"""
    drt = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    perfil_acesso = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('nome',)
        verbose_name_plural = 'Logins'

    """Representação em texto do objeto"""
    def __str__(self):
        return f"{self.drt} - {self.nome}"


class City(models.Model):
    """Classe não utilizada no projeto Novo Portal de Procedimentos"""
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "cities"
    
    """Representação em texto do objeto"""
    def __str__(self):
        return self.name
    
