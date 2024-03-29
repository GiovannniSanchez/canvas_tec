# Generated by Django 4.2 on 2023-09-08 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backds', '0022_rename_data_total_invercion_data_corrida_financiera_data_total_inversion'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCredential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'EmailCredential',
                'verbose_name_plural': 'EmailCredentials',
                'db_table': 'email_credential',
                'ordering': ['id'],
            },
        ),
    ]
