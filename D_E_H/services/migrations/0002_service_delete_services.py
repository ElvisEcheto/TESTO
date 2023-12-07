# Generated by Django 4.2.7 on 2023-12-07 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Price', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]
