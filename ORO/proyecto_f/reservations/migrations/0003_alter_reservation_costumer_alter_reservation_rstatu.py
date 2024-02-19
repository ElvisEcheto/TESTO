# Generated by Django 5.0.1 on 2024-02-18 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumers', '0001_initial'),
        ('reservations', '0002_reservation_coder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='costumer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='costumers.costumer'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='rstatu',
            field=models.CharField(default='Reservado', max_length=200),
        ),
    ]
