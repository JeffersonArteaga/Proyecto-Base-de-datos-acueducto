# Generated by Django 4.2 on 2023-04-29 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_delete_miusuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.CharField(max_length=255)),
                ('monto', models.IntegerField(max_length=255)),
            ],
        ),
    ]
