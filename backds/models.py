from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class answers_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=False)
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

    def __str__(self):
        return self.answer1

    class Meta:
        db_table='answers_user'
        verbose_name='Respuesta_Usuario'
        verbose_name_plural='Respuestas_usuario'
        ordering=['id']
