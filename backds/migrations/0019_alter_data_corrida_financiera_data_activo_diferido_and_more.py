# Generated by Django 4.2 on 2023-09-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backds', '0018_data_corrida_financiera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_corrida_financiera',
            name='data_activo_diferido',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='data_corrida_financiera',
            name='data_activo_fijo',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='data_corrida_financiera',
            name='data_capital_trabajo_mano_obra',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='data_corrida_financiera',
            name='data_capital_trabajo_servicios',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='data_corrida_financiera',
            name='data_capital_trabajo_servicios_mantto',
            field=models.JSONField(null=True),
        ),
    ]
