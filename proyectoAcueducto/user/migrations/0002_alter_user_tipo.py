# Generated by Django 4.2 on 2023-05-03 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tipo',
            field=models.ForeignKey(limit_choices_to={'estado': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.tipo'),
        ),
    ]
