# Generated by Django 4.2 on 2023-05-02 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0019_alter_item_grupo_acesso'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='usuario',
            field=models.CharField(default='Usuario1', max_length=50, verbose_name='Usuário'),
        ),
    ]
