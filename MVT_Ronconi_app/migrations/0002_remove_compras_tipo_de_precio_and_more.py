# Generated by Django 4.1.3 on 2022-12-01 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MVT_Ronconi_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compras',
            name='tipo_de_precio',
        ),
        migrations.RemoveField(
            model_name='ventas',
            name='tipo_de_precio',
        ),
    ]