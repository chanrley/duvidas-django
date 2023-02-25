# Generated by Django 4.1.7 on 2023-02-25 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novo_portal_dva', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novo_portal_dva.menu')),
            ],
            options={
                'verbose_name_plural': 'SubMenus',
                'ordering': ('nome',),
            },
        ),
    ]
