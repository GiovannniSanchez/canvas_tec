from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Questionnaire(models.Model):
    question1 = models.TextField(max_length=100)
    question2 = models.TextField(max_length=100)
    question3 = models.TextField(max_length=100)
    question4 = models.TextField(max_length=100)
    question5 = models.TextField(max_length=100)

class AnswersChatgpt(models.Model):
    user=models.CharField(User, on_delete=models.CASCADE, null=True, blank=False)
    problema=models.TextField(max_length=700, unique=False, verbose_name='problema')
    cliente_ideal=models.TextField(max_length=700, unique=False, verbose_name='cliente_ideal')
    propuesta_valor=models.TextField(max_length=700, unique=False, verbose_name='propuesta_valor')
    soluciones=models.TextField(max_length=700, unique=False, verbose_name='soluciones')
    canal=models.TextField(max_length=700, unique=False, verbose_name='canal')
    flujo_ingresos=models.TextField(max_length=700, unique=False, verbose_name='flujo_ingresos')
    estructura_costes=models.TextField(max_length=700, unique=False, verbose_name='estructura_costes')
    metricas=models.TextField(max_length=700, unique=False, verbose_name='metricas')
    ventaja_diferencial=models.TextField(max_length=700, unique=False, verbose_name='ventaja_diferencial')

    def __str__(self):
        return self.problema

    class Meta:
        db_table='answer_chatgpt'
        verbose_name='Respuesta_Chatgpt'
        verbose_name_plural='Respuestas_Chatgpt'
        ordering=['id']