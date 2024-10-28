from django.db import migrations

def add_initial_asientos(apps, schema_editor):
    Asiento = apps.get_model('asientos', 'Asiento')
    asientos_iniciales = [
        '1A', '1B', '1C', '1D',
        '2A', '2B', '2C', '2D',
        '3A', '3B', '3C', '3D',
        '4A', '4B', '4C', '4D',
        '5A', '5B', '5C', '5D'
    ]
    for numero in asientos_iniciales:
        Asiento.objects.create(numero_asiento=numero)

class Migration(migrations.Migration):

    dependencies = [
        ('asientos', '0007_remove_asiento_estado'),  # Cambia esto según tu última migración en `asientos`
    ]

    operations = [
        migrations.RunPython(add_initial_asientos),
    ]