# Generated by Django 5.1 on 2024-08-22 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lernorte', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lernort',
            name='bild1',
        ),
        migrations.RemoveField(
            model_name='lernort',
            name='bild2',
        ),
        migrations.RemoveField(
            model_name='lernort',
            name='bild3',
        ),
        migrations.RemoveField(
            model_name='lernort',
            name='kml_file',
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bild1', models.ImageField(upload_to='lernorte/pictures')),
                ('bild2', models.ImageField(upload_to='lernorte/pictures')),
                ('bild3', models.ImageField(upload_to='lernorte/pictures')),
                ('kml_file', models.FileField(upload_to='lernorte/kml_files')),
                ('lernort', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lernorte.lernort')),
            ],
        ),
    ]
