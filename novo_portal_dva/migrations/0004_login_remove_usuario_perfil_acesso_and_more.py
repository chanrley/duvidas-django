# Generated by Django 4.1.7 on 2023-03-17 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novo_portal_dva', '0003_grupoacesso_alter_submenu_options_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drt', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('perfil_acesso', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Logins',
                'ordering': ('nome',),
            },
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='perfil_acesso',
        ),
        migrations.DeleteModel(
            name='GrupoAcesso',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]