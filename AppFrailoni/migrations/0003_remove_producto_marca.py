# Generated by Django 4.1.3 on 2022-12-19 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFrailoni', '0002_rename_nombrecliente_cliente_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='marca',
        ),
    ]
