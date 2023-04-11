from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name='Home'),
    path('about/',views.about,name='About'),
    path('prueba/',views.prueba,name='Chatgpt'),
    path('formulario/',views.formulario,name='Fomulario'),
    path('test01/',views.test01,name='test01'),
    path('table/',views.table,name='table'),
    path('canvas/',views.canvas,name='canvas')

]