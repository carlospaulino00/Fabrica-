# Generated by Django 4.1.7 on 2023-04-01 22:11

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_postoatendimento_nome_postoatendimento_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postoatendimento',
            name='nome',
            field=models.CharField(default='nome do cliente', max_length=50, verbose_name=app.models.Cliente),
        ),
    ]