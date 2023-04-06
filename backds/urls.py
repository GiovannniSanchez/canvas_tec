from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name='Home'),
    path('about/',views.about,name='About'),
    path('prueba/',views.prueba,name='Chatgpt'),
    path('formulario/',views.formulario,name='Fomulario')

]