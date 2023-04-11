from django.urls import path
from . import views


urlpatterns = [
path('cuestionario/', views.cuestionario, name='cuestionario')
    ]