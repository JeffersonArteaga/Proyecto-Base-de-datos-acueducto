# Generated by Django 4.2 on 2023-04-29 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_cuenta_direccion_miusuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MiUsuario',
        ),
    ]
