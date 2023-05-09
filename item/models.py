from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from usuario.models import GrupoAcesso

class Category(models.Model):
    """Tipos de categorias de um Item(Publicação) """
    name = models.CharField(max_length=255)

    class Meta:
        """Ordenando alfabéticamente por name """
        ordering = ('name',)
        """Nome no plural"""
        verbose_name_plural = 'Categorias'
    
    """Representação textual do objeto """
    def __str__(self):
        return self.name

class Item(models.Model):# Publicação
    """Isso é um objeto do tipo Publicação que só pode ser feita pelos perfis 1 ou 3"""

    category = models.ForeignKey(Category, verbose_name='Categoria', related_name='items', on_delete=models.CASCADE, blank=False)
    name = models.CharField( verbose_name='Título', max_length=255, blank=False)
    description = models.TextField(verbose_name='Descrição curta', blank=False, null=True)
    description_with_photo = RichTextUploadingField(verbose_name='Descrição longa / com foto', blank=False, null=True)
    price = models.FloatField(default=1)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    is_published = models.BooleanField(verbose_name='Deseja publicar?', default=True)
    created_by = models.ForeignKey(User, verbose_name='Criado por', related_name='items', on_delete=models.CASCADE)
    usuario = models.CharField(max_length=50, verbose_name='Usuário', default='Usuario1')
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    grupo_acesso = models.ForeignKey(to=GrupoAcesso, on_delete=models.CASCADE, default=2, verbose_name='Setor')

    
    class Meta:
        """Ordem decrescente por data de criação"""
        ordering = ['-created_at']
    
    """Representação textual do objeto """
    def __str__(self):
        return self.name

    

class Post(models.Model):
    """Isso é um objeto do tipo Post, mas foi só um exemplo de base para iniciar o projeto e para testar as funcionalidades da biblioteca CKEditor"""
    
    title = models.CharField(max_length=255)
    body1 = models.TextField(blank=True, null=True)
    body2 = RichTextField(blank=True, null=True)
    body3 = RichTextUploadingField(blank=True, null=True)
