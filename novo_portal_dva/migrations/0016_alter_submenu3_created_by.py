# Generated by Django 4.2 on 2023-05-17 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novo_portal_dva', '0015_submenu3_created_at_submenu3_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenu3',
            name='created_by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]