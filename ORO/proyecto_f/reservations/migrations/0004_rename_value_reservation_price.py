# Generated by Django 5.0.1 on 2024-02-18 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_alter_reservation_costumer_alter_reservation_rstatu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='value',
            new_name='price',
        ),
    ]
