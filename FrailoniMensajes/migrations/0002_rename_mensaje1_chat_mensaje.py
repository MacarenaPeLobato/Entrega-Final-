# Generated by Django 4.1.3 on 2023-01-22 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FrailoniMensajes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='mensaje1',
            new_name='mensaje',
        ),
    ]