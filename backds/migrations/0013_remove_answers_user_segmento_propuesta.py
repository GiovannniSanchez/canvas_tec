# Generated by Django 4.2 on 2023-08-29 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backds', '0012_remove_answerschatgpt_actividades_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers_user',
            name='segmento_propuesta',
        ),
    ]
