# Generated by Django 4.2 on 2023-05-17 16:04

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_grupoacesso_publicador'),
        ('novo_portal_dva', '0014_submenu_grupo_acesso'),
    ]

    operations = [
        migrations.AddField(
            model_name='submenu3',
            name='created_at',
            field=models.TimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='submenu3',
            name='created_by',
            field=models.ForeignKey(default=19, on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario'),
        ),
        migrations.AddField(
            model_name='submenu3',
            name='description_with_photo',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
