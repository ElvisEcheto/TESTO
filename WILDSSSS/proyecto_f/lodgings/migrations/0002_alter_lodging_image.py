# Generated by Django 5.0.1 on 2024-01-28 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodgings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lodging',
            name='image',
            field=models.ImageField(null=True, upload_to='static/lodgings_images'),
        ),
    ]