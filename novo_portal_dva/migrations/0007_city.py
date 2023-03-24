# Generated by Django 4.1.7 on 2023-03-23 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novo_portal_dva', '0006_delete_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
    ]
