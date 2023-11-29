# Generated by Django 4.2.7 on 2023-11-29 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=50)),
                ('Document_type', models.CharField(max_length=20)),
                ('Document', models.IntegerField(unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
    ]