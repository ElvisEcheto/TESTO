# Generated by Django 5.0.1 on 2024-03-11 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumers', '0002_remove_costumer_typedocument'),
        ('reservations', '0005_remove_reservation_coder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='costumer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='costumers.costumer'),
        ),
    ]
