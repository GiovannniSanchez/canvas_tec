# Generated by Django 4.2 on 2023-08-29 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backds', '0014_generatedimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='generatedimage',
            options={'ordering': ['id'], 'verbose_name': 'GeneratedImage', 'verbose_name_plural': 'GeneratedImages'},
        ),
        migrations.AlterModelTable(
            name='generatedimage',
            table='GeneratedImages',
        ),
    ]