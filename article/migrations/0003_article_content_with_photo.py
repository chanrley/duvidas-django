# Generated by Django 4.2 on 2023-04-12 13:14

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_options_article_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_with_photo',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
