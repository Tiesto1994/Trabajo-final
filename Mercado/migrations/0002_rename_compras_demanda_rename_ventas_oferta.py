# Generated by Django 4.1.3 on 2023-01-19 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mercado', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='compras',
            new_name='demanda',
        ),
        migrations.RenameModel(
            old_name='ventas',
            new_name='oferta',
        ),
    ]
