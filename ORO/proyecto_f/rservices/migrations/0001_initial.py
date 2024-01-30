# Generated by Django 5.0.1 on 2024-01-30 00:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservations', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reservations.reservation')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='services.service')),
            ],
        ),
    ]