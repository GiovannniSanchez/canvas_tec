# Generated by Django 4.2 on 2023-04-17 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backds', '0002_rename_id_user_answers_user_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answers_user',
            options={'ordering': ['id'], 'verbose_name': 'AnswerChatgpt', 'verbose_name_plural': 'AnswersChatgpt'},
        ),
        migrations.AlterField(
            model_name='answers_user',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AnswersChatgpt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problema', models.TextField(max_length=700, verbose_name='problema')),
                ('cliente_ideal', models.TextField(max_length=700, verbose_name='cliente_ideal')),
                ('propuesta_valor', models.TextField(max_length=700, verbose_name='propuesta_valor')),
                ('soluciones', models.TextField(max_length=700, verbose_name='soluciones')),
                ('canal', models.TextField(max_length=700, verbose_name='canal')),
                ('flujo_ingresos', models.TextField(max_length=700, verbose_name='flujo_ingresos')),
                ('estructura_costes', models.TextField(max_length=700, verbose_name='estructura_costes')),
                ('metricas', models.TextField(max_length=700, verbose_name='metricas')),
                ('ventaja_diferencial', models.TextField(max_length=700, verbose_name='ventaja_diferencial')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backds.answers_user')),
            ],
            options={
                'verbose_name': 'Respuesta_Chatgpt',
                'verbose_name_plural': 'Respuestas_Chatgpt',
                'db_table': 'answer_chatgpt',
                'ordering': ['id'],
            },
        ),
    ]
