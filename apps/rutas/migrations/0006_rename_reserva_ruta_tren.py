# Generated by Django 5.1.2 on 2024-10-27 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0005_remove_ruta_tren_ruta_reserva_alter_ruta_destino_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ruta',
            old_name='reserva',
            new_name='tren',
        ),
    ]
