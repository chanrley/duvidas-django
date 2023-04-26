from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):# Publicação
    category = models.ForeignKey(Category, verbose_name='Categoria', related_name='items', on_delete=models.CASCADE, blank=False)
    name = models.CharField( verbose_name='Título', max_length=255, blank=False)
    description = models.TextField(verbose_name='Descrição curta', blank=False, null=True)
    description_with_photo = RichTextUploadingField(verbose_name='Descrição longa / com foto', blank=False, null=True)
    price = models.FloatField(default=1)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    is_published = models.BooleanField(verbose_name='Deseja publicar?', default=True)
    created_by = models.ForeignKey(User, verbose_name='Criado por', related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

    

class Post(models.Model):
    title = models.CharField(max_length=255)
    body1 = models.TextField(blank=True, null=True)
    body2 = RichTextField(blank=True, null=True)
    body3 = RichTextUploadingField(blank=True, null=True)
