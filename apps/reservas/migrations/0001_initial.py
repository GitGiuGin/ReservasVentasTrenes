# Generated by Django 3.2 on 2024-09-20 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trenes', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reserva', models.DateField(verbose_name='Fecha de Reserva')),
                ('estado', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('tren', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trenes.tren')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
                'db_table': 'reserva',
                'ordering': ['fecha_reserva', 'cliente'],
            },
        ),
    ]
