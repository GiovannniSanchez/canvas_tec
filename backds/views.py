from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import answers_user, AnswersChatgpt
from .forms import RegisterAnswer
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import openai


def about(request):
    return render(request, 'about.html')


@login_required
def prueba(request):
    user = request.user

    last=answers_user.objects.filter(user=user).last()

    answers_list = [
        last.answer1,
        last.answer2,
        last.answer3,
        last.answer4,
        last.answer5,
        last.answer6,
        last.answer7,
        last.answer8,
        last.answer9,
        last.answer10
    ]

    # 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
    openai.api_key = "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"

    # Contexto del asistente
    messages = [{"role": "system", "content": "Eres un experto en modelos de negocio"}]

    preguntas = [
        '¿Que ofreces al mercado?: ',
        '¿Sabes como elaborarlo?: ',
        '¿Como te conoceran tus clientes?: ',
        '¿Que problema resuelve?: ',
        '¿Cuanto va a costar?: ',
        '¿Como lo vas a vender?: ',
        '¿A quien lo vas a vender?: ',
        '¿Existen alternativas a tu producto o servicio?: ',
        '¿Que hace a tu producto diferente?: ',
        '¿porque los clientes compraran lo que ofreces?: '
    ]


    prompt_default = 'una herramienta de planificación empresarial lean canvas que consta de nueve bloques:'\
                     'problema,' \
                     ' soluciones,' \
                     ' propuesta de valor,' \
                     ' ventaja diferiencial,' \
                     ' métricas,' \
                     ' cliente ideal,' \
                     ' canales' \
                     ' estructura de costos y' \
                     'flujo de ingresos'

    prompt_default1 = 'puedes darme el segmento de clientes segun tu interpretacion como experto en modelo de negocios' \
                      'haciendo referencia a las siguientes preguntas con sus respectivas respuestas y me lo puedes dar en un formato corto y en forma de lista en caso de llevar' \
                      'varios puntos?: '

    prompt_default2= 'Ahora segun la estructura anterior puedes darme el  "problema"?'

    prompt_default3= 'Ahora segun la estructura anterior, puedes darme la "Propuesta de valor"?'

    prompt_default4=  'Ahora segun la estrctura anterior puedes darme las "soluciones"?'

    prompt_default5=  'Ahora segun la estrctura anterior puedes darme los "canales"?'

    prompt_default6=  'Ahora segun la estrctura anterior puedes darme el "flujo de ingresos"?'

    prompt_default7=  'Ahora segun la estrctura anterior puedes darme la "estructura de costes"?'

    prompt_default8=  'Ahora segun la estrctura anterior puedes darme las "metricas"'


    prompt_default9= 'Ahora segun la estrctura anterior puedes darme la "ventaja diferencial"?'



    preg_resp = '\n'.join([
        f"{preguntas[i]}{str(answers_list[i])}"
        for i in range(len(preguntas))
    ])
#////////////////////////////////////////////////////////////////////////////////////////
    contenido = prompt_default+prompt_default1+preg_resp
    messages.append({"role": "user", "content": contenido})
    respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=300)
    contenido_respuesta = respuesta.choices[0].message.content
    #///////////////////////////////////////////////////////////////////////////////////////////
    contenido1 =prompt_default+prompt_default2+preg_resp

    messages.append({"role": "user", "content": contenido1})
    respuesta1 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=300)
    contenido_respuesta1 = respuesta1.choices[0].message.content
    #////////////////////////////////////////////////////////////////////////////////////////////////////
    contenido2 =prompt_default+prompt_default3+preg_resp

    messages.append({"role": "user", "content": contenido2})
    respuesta2 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=300)
    contenido_respuesta2 = respuesta2.choices[0].message.content
    # Guardar la respuesta en la base de datos
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    contenido3 =prompt_default+prompt_default4+preg_resp

    messages.append({"role": "user", "content": contenido3})
    respuesta3 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=300)
    contenido_respuesta3 = respuesta3.choices[0].message.content
    #/////////////////////////////////////////////////////////////////////////////////////////////////////7
    contenido4 =prompt_default+prompt_default5+preg_resp

    messages.append({"role": "user", "content": contenido4})
    respuesta4 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=300)
    contenido_respuesta4 = respuesta4.choices[0].message.content
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////
    contenido5 =prompt_default+prompt_default6+preg_resp

    messages.append({"role": "user", "content": contenido5})
    respuesta5 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=300)
    contenido_respuesta5 = respuesta5.choices[0].message.content
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////
    contenido6 =prompt_default+prompt_default7+preg_resp

    messages.append({"role": "user", "content": contenido6})
    respuesta6 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=300)
    contenido_respuesta6 = respuesta6.choices[0].message.content
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////
    contenido7 =prompt_default+prompt_default8+preg_resp

    messages.append({"role": "user", "content": contenido7})
    respuesta7 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=300)
    contenido_respuesta7 = respuesta7.choices[0].message.content
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////
    contenido8 =prompt_default+prompt_default9+preg_resp
    messages.append({"role": "user", "content": contenido8})
    respuesta8 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=300)
    contenido_respuesta8 = respuesta8.choices[0].message.content
    #Guardar la respuesta en la base de datos
    answer_chat = AnswersChatgpt.objects.create(user=user,
                                                cliente_ideal=contenido_respuesta,
                                                problema=contenido_respuesta1,
                                                propuesta_valor=contenido_respuesta2,
                                                soluciones=contenido_respuesta3,
                                                canal=contenido_respuesta4,
                                                flujo_ingresos=contenido_respuesta5,
                                                estructura_costes=contenido_respuesta6,
                                                metricas=contenido_respuesta7,
                                                ventaja_diferencial=contenido_respuesta8
                                                )
    answer_chat.save()
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////

    return redirect('canvas')

@login_required
def formulario(request):
    if request.method == 'GET':
        return render(request, 'formulario.html', {'form': RegisterAnswer()})
    else:

        user_id = request.user.id
        answers_user.objects.create(name_e_p=request.POST['name_e_p'],
                                    answer1=request.POST['answer1'],
                                    answer2=request.POST['answer2'],
                                    answer3=request.POST['answer3'],
                                    answer4=request.POST['answer4'],
                                    answer5=request.POST['answer5'],
                                    answer6=request.POST['answer6'],
                                    answer7=request.POST['answer7'],
                                    answer8=request.POST['answer8'],
                                    answer9=request.POST['answer9'],
                                    answer10=request.POST['answer10'], user_id=user_id)
        return redirect('Chatgpt')


@login_required
def test01(request):
    user = request.user
    answers = answers_user.objects.filter(user=user)
    return render(request, 'test01.html',{'respuestas':answers})


@login_required
def canvas(request):
    try:
        user = request.user
        last = AnswersChatgpt.objects.filter(user=user).last()
        lastname = answers_user.objects.filter(user=user).last()
        proyect_name = lastname.name_e_p

        answers_canvas = [
            last.problema,
            last.cliente_ideal,
            last.propuesta_valor,
            last.soluciones,
            last.canal,
            last.flujo_ingresos,
            last.estructura_costes,
            last.metricas,
            last.ventaja_diferencial,
        ]

        return render(request, 'canvas.html', {
            'respuestas_canvas': answers_canvas,
            'nombre': proyect_name
        })

    except AttributeError:
        # Manejo del error
        answers_canvas = []  # O cualquier otra lógica que desees utilizar en caso de error
        proyect_name = None  # O cualquier otro valor o lógica que desees utilizar en caso de error

        return render(request, 'canvas.html', {
            'respuestas_canvas': answers_canvas,
            'nombre': proyect_name
        })

import requests
import pandas as pd

def obtener_datos_inegi(clave_api, indicador_id):
    # URL base de la API del INEGI
    url_base = "https://api.datos.gob.mx/v2/"

    # Endpoint para obtener los datos de un indicador específico
    endpoint = f"series/{indicador_id}/datos"

    # Parámetros de la consulta
    params = {
        "token": clave_api,
        "pageSize": 10  # Número de resultados a obtener
    }

    # Realizar la solicitud GET a la API del INEGI
    try:
        response = requests.get(url_base + endpoint, params=params)
        response.raise_for_status()  # Verificar si hubo errores en la respuesta

        # Obtener los datos de la respuesta en formato JSON
        datos = response.json()

        # Crear un DataFrame de pandas con los datos
        df = pd.DataFrame(datos["datos"])

        # Procesar y manipular los datos como desees
        # Por ejemplo, puedes realizar operaciones de limpieza, transformación, filtrado, etc.
        # Aquí hay un ejemplo de cómo imprimir las fechas y valores del DataFrame
        for index, row in df.iterrows():
            fecha = row["fecha"]
            valor = row["dato"]
            print(f"Fecha: {fecha}, Valor: {valor}")

        # También puedes realizar otros análisis y manipulaciones con pandas

    except requests.exceptions.RequestException as e:
        print("Error en la solicitud:", e)

# Ejemplo de uso
clave_api = "TU_CLAVE_API_DEL_INEGI"
indicador_id = "INDICADOR_ID_DESEADO"

obtener_datos_inegi(clave_api, indicador_id)
