# Generated by Django 4.2 on 2023-09-08 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backds', '0023_emailcredential'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_corrida_financiera',
            name='data_memorias_calculo',
            field=models.JSONField(null=True),
        ),
    ]
