# Generated by Django 4.1.3 on 2023-02-15 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MVT_Ronconi_app', '0004_chatconsulta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatconsulta',
            old_name='apellido',
            new_name='Apellido',
        ),
    ]