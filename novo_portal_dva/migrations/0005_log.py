# Generated by Django 4.1.7 on 2023-03-20 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novo_portal_dva', '0004_login_remove_usuario_perfil_acesso_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo', models.TextField()),
                ('data_insercao', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
