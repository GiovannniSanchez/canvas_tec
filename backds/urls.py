from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.about,name='About'),
    path('prueba/',views.prueba,name='Chatgpt'),
    path('formulario/',views.formulario,name='Formulario'),
    path('test01/',views.test01,name='test01'),
    path('canvas/',views.canvas,name='canvas'),
    path('obtener_datos_inegi/',views.obtener_datos_inegi,name='data'),
    path('resultado_inegi/<str:inegi_code>/<str:nombre_indicador>/<str:valor_consulta>/<str:cantidad>/<str:nombres_ids>/', views.resultado_inegi, name='resultado_inegi'),
]
