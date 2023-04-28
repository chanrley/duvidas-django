# Generated by Django 4.2 on 2023-04-28 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_grupoacesso_publicador'),
        ('item', '0017_item_grupo_acesso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='grupo_acesso',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='usuario.grupoacesso', verbose_name='Grupo de Acesso'),
        ),
    ]
