# Generated by Django 5.1.2 on 2024-10-28 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asientos', '0005_alter_asiento_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asiento',
            name='reserva',
        ),
    ]
