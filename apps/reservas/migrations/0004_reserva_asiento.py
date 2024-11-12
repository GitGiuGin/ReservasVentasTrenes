# Generated by Django 5.1.2 on 2024-10-28 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asientos', '0006_remove_asiento_reserva'),
        ('reservas', '0003_alter_reserva_fecha_reserva'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='asiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asientos', to='asientos.asiento'),
        ),
    ]
