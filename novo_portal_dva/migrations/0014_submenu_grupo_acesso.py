# Generated by Django 4.2 on 2023-05-15 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_grupoacesso_publicador'),
        ('novo_portal_dva', '0013_alter_menu_options_menu_grupo_acesso_delete_setor'),
    ]

    operations = [
        migrations.AddField(
            model_name='submenu',
            name='grupo_acesso',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='usuario.grupoacesso'),
        ),
    ]
