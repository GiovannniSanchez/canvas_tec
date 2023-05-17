from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class answers_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    name_e_p=models.TextField(max_length=30, unique=False, verbose_name='Nombre_empresa_proyecto')
    answer1=models.TextField(max_length=1000, unique=False, verbose_name='Respuesta1')
    answer2=models.TextField(max_length=1000, unique=False, verbose_name='Respuesta2')
    answer3=models.TextField(max_length=1000, unique=False, verbose_name='Respuesta3')
    answer4=models.TextField(max_length=1000, unique=False, verbose_name='Respuesta4')
    answer5=models.TextField(max_length=1000, unique=False, verbose_name='Respuesta5')
    answer6=models.TextField(max_length=1000, unique=False, verbose_name='Respuesta6')
    answer7=models.TextField(max_length=1000, unique=False, verbose_name='Respuesta7')
    answer8=models.TextField(max_length=1000, unique=False, verbose_name='Respuesta8')
    answer9=models.TextField(max_length=1000, unique=False, verbose_name='Respuesta9')
    answer10=models.TextField(max_length=1000, unique=False, verbose_name='Respuesta10')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer1

    class Meta:
        db_table='answers_user'
        verbose_name='AnswerChatgpt'
        verbose_name_plural='AnswersChatgpt'
        ordering=['id']

class AnswersChatgpt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    problema = models.TextField(max_length=700, unique=False, verbose_name='problema')
    cliente_ideal = models.TextField(max_length=1000, unique=False, verbose_name='cliente_ideal')
    propuesta_valor = models.TextField(max_length=700, unique=False, verbose_name='propuesta_valor')
    soluciones = models.TextField(max_length=700, unique=False, verbose_name='soluciones')
    canal = models.TextField(max_length=700, unique=False, verbose_name='canal')
    flujo_ingresos = models.TextField(max_length=700, unique=False, verbose_name='flujo_ingresos')
    estructura_costes = models.TextField(max_length=700, unique=False, verbose_name='estructura_costes')
    metricas = models.TextField(max_length=700, unique=False, verbose_name='metricas')
    ventaja_diferencial = models.TextField(max_length=700, unique=False, verbose_name='ventaja_diferencial')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.problema

    class Meta:
        db_table='answer_chatgpt'
        verbose_name='Respuesta_Chatgpt'
        verbose_name_plural='Respuestas_Chatgpt'
        ordering=['id']
