# Generated by Django 4.2 on 2023-04-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0013_item_is_published_alter_item_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Deseja publicar?'),
        ),
    ]
