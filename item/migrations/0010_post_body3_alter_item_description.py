# Generated by Django 4.2 on 2023-04-11 11:52

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_alter_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body3',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
