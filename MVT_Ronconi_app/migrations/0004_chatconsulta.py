# Generated by Django 4.1.3 on 2023-02-15 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MVT_Ronconi_app', '0003_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='chatconsulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('Telefono', models.IntegerField()),
                ('Mensaje', models.CharField(max_length=500)),
            ],
        ),
    ]