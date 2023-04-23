from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.about,name='About'),
    path('prueba/',views.prueba,name='Chatgpt'),
    path('formulario/',views.formulario,name='Formulario'),
    path('test01/',views.test01,name='test01'),
    path('canvas/',views.canvas,name='canvas')
]