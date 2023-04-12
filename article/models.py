from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    content_with_photo = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at',]