# Generated by Django 4.2 on 2023-09-05 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backds', '0019_alter_data_corrida_financiera_data_activo_diferido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_corrida_financiera',
            name='data_total_inversion',
            field=models.JSONField(null=True),
        ),
    ]
