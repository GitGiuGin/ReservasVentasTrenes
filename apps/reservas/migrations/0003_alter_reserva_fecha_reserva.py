# Generated by Django 5.1.2 on 2024-10-27 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_remove_reserva_tren_reserva_ruta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha_reserva',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Reserva'),
        ),
    ]
