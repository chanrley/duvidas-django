# Generated by Django 4.1.7 on 2023-03-17 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoAcesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo_acesso', models.IntegerField()),
                ('nome_grupo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Grupos de acesso',
                'ordering': ('nome_grupo',),
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drt', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('perfil_acesso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.grupoacesso')),
            ],
            options={
                'verbose_name_plural': 'Usuários',
                'ordering': ('nome',),
            },
        ),
    ]
