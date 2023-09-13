from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class answers_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    name_e_p=models.TextField(max_length=30, unique=False, verbose_name='Nombre_empresa_proyecto')
    segmento=models.TextField(max_length=1000, unique=False, verbose_name='segmento')
    propuesta=models.TextField(max_length=1000, unique=False, verbose_name='propuesta')
    canales=models.TextField(max_length=1000, unique=False, verbose_name='canales')
    relaciones=models.TextField(max_length=1000, unique=False, verbose_name='relaciones')
    recursos=models.TextField(max_length=1000, unique=False, verbose_name='recursos')
    actividades=models.TextField(max_length=1000, unique=False, verbose_name='actividades')
    socios=models.TextField(max_length=1000, unique=False, verbose_name='socios')
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
    segmento_gpt = models.TextField(max_length=1000, unique=False, verbose_name='segmento_gpt')
    propuesta_gpt = models.TextField(max_length=700, unique=False, verbose_name='propuesta_gpt')
    canales_gpt = models.TextField(max_length=700, unique=False, verbose_name='canales_gpt')
    relaciones_gpt = models.TextField(max_length=700, unique=False, verbose_name='relaciones_gpt')
    recursos_gpt = models.TextField(max_length=700, unique=False, verbose_name='recursos_gpt')
    actividades_gpt = models.TextField(max_length=700, unique=False, verbose_name='actividades_gpt')
    socios_gpt = models.TextField(max_length=700, unique=False, verbose_name='socios_gpt')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Generated {self.id}"

    class Meta:
        db_table='answer_chatgpt'
        verbose_name='Respuesta_Chatgpt'
        verbose_name_plural='Respuestas_Chatgpt'
        ordering=['id']


class GeneratedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    segmento_image1 = models.URLField(max_length=1000, null=True)
    segmento_image2 = models.URLField(max_length=1000, null=True)
    propuesta_image1 = models.URLField(max_length=1000, null=True)
    propuesta_image2 = models.URLField(max_length=1000, null=True)
    canales_image = models.URLField(max_length=1000, null=True)
    relaciones_image = models.URLField(max_length=1000, null=True)
    recursos_image = models.URLField(max_length=1000, null=True)
    actividades_image = models.URLField(max_length=1000, null=True)
    socios_image1 = models.URLField(max_length=1000, null=True)
    socios_image2 = models.URLField(max_length=1000, null=True)
    ingresos_image = models.URLField(max_length=1000, null=True)
    costos_image = models.URLField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Generated Image {self.id}"

    class Meta:
        db_table = 'GeneratedImages'
        verbose_name = 'GeneratedImage'
        verbose_name_plural = 'GeneratedImages'
        ordering = ['id']

class LogoProyect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    logo = models.ImageField(upload_to='logo_images')
    load_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.logo.url

    class Meta:
        db_table = 'logo_proyect'
        verbose_name = 'logo_proyect'
        verbose_name_plural = 'logos_proyects'
        ordering = ['id']

class data_corrida_financiera(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    data_activo_fijo = models.JSONField(null=True)
    data_activo_diferido = models.JSONField(null=True)
    data_capital_trabajo_mano_obra = models.JSONField(null=True)
    data_capital_trabajo_servicios = models.JSONField(null=True)
    data_capital_trabajo_servicios_mantto = models.JSONField(null=True)
    data_memorias_calculo = models.JSONField(null=True)
    data_total_inversion = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Generated  {self.id}"

    class Meta:
        db_table = 'corrida_financiera'
        verbose_name = 'corrida_financiera'
        verbose_name_plural = 'corridas_financieras'
        ordering = ['id']

