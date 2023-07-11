from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import answers_user, AnswersChatgpt
from .forms import RegisterAnswer
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import openai
import pandas as pd
import requests
import json
from fuzzywuzzy import fuzz
from urllib.parse import urlencode
from django.urls import reverse


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
    respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=messages, max_tokens=300)
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




def obtener_datos_inegi(request):
    if request.method == 'GET':
        return render(request, 'pruebadata.html')
    else:
        ruta = 'C:/Users/ghost/canvas_tec/datos.json'
        # Abrir el archivo JSON
        with open(ruta, 'r') as file:
            # Cargar el contenido del archivo JSON
            contenido_json = json.load(file)

        var = request.POST.get('var')
        inegi_code = ""
        nombre_indicador = ""
        var1 = var.lower()  # Transformar en minúscula el valor de la variable
        max_similarity = 0

        for item in contenido_json['CODE']:
            description_lower = item['Description'].lower()
            keywords = var1.split()  # Obtener palabras clave de la búsqueda
            similarity = sum(fuzz.partial_ratio(keyword, description_lower) for keyword in keywords)
            if similarity > max_similarity:
                max_similarity = similarity
                inegi_code = item['value']
                nombre_indicador = item['Description']  # Asignar el valor de "Description" a la variable "nombre_indicador"
                print("$$$$$$", nombre_indicador, "$$$$$end")
                print("!!!!!!!!!", inegi_code, "!!!!!!!end")

        # /////////////////////////////////////////////////////////////////////////////////////
        # consulta inegi

        url_base = "https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/"
        indicador = inegi_code
        idioma = "/es/"
        Area_geografica = "22/"
        url_base_final = "true/BISE/2.0/9fde1331-f4c3-4d45-95d6-e455a1aa9615?type=json"

        url_completa = url_base + indicador + idioma + Area_geografica + url_base_final
        print(url_completa)

        response = requests.get(url_completa)
        data_json = response.json()

        # Cálculo de valor_consulta
        valor_consulta = None
        if "Series" in data_json and isinstance(data_json["Series"], list):
            series = data_json["Series"]
            for serie in series:
                if "OBSERVATIONS" in serie and isinstance(serie["OBSERVATIONS"], list):
                    observations = serie["OBSERVATIONS"]
                    for observation in observations:
                        if "OBS_VALUE" in observation:
                            valor_consulta = round(float(observation["OBS_VALUE"]), 2)
                            break
        print(valor_consulta)

        params = urlencode({'data_json': json.dumps(data_json)})  # Convertir a JSON y codificar como parámetro de consulta

        if inegi_code:
            url = reverse('resultado_inegi', kwargs={'inegi_code': indicador, 'nombre_indicador': nombre_indicador, 'valor_consulta': valor_consulta})
            return redirect(url)
        else:
            message = "Valor no encontrado"
            return redirect('resultado_inegi', inegi_code=message)
def resultado_inegi(request, inegi_code=None, nombre_indicador=None, valor_consulta=None):
    data_json_str = request.GET.get('data_json')
    data_json = json.loads(data_json_str) if data_json_str else None

    context = {
        'data': inegi_code,
        'name': nombre_indicador,
        'valor_consulta': valor_consulta
    }
    return render(request, 'prueba_inegi.html', context)