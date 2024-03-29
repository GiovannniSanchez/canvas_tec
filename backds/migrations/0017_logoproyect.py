# Generated by Django 4.2 on 2023-08-31 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backds', '0016_alter_generatedimage_actividades_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoProyect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo_images')),
                ('load_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'logo_proyect',
                'verbose_name_plural': 'logos_proyects',
                'db_table': 'logo_proyect',
                'ordering': ['id'],
            },
        ),
    ]
