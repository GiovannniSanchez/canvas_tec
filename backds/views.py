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

        #///////////////////////////////////////////////////////////////////////////////////////////////////////
        #CONSULTA API DENUE
        var_denue = request.POST.get('var_denue')
        url_base = "https://www.inegi.org.mx/app/api/denue/v1/consulta/BuscarEntidad/"
        condicion = var_denue
        entidad = "/22"
        inicio = "/1"
        cantidad = "/3/"
        token = "9fde1331-f4c3-4d45-95d6-e455a1aa9615"

        url_completa = url_base + condicion + entidad + inicio + cantidad + token

        response = requests.get(url_completa)

        data_json = response.json()

        sumatoria_ids = {}
        nombres_ids = {}

        # Almacenar el nombre de cada ID
        for establecimiento in data_json:
            id_establecimiento = establecimiento["Id"]
            nombre_establecimiento = establecimiento["Nombre"]

            sumatoria_ids[id_establecimiento] = 1

            nombres_ids[id_establecimiento] = nombre_establecimiento

        # Imprimir la sumatoria y el nombre de cada ID
        for id_establecimiento, sumatoria in sumatoria_ids.items():
            nombre = nombres_ids[id_establecimiento]
            print(f"ID: {id_establecimiento}, Nombre: {nombre}")

        print("///////////7")
        cantidad = len(data_json)
        print(cantidad)
        print(nombre)
#//////////////////////////////////////////////////////////////////////////////////////7
        params = urlencode({'data_json': json.dumps(data_json)})  # Convertir a JSON y codificar como parámetro de consulta

        if inegi_code:
            url = reverse('resultado_inegi', kwargs={'inegi_code': indicador, 'nombre_indicador': nombre_indicador,
                                                     'valor_consulta': valor_consulta, 'cantidad': cantidad,
                                                     'nombres_ids': nombres_ids})
            return redirect(url)
        else:
            message = "Valor no encontrado"
            return redirect('resultado_inegi', inegi_code=message)
def resultado_inegi(request, inegi_code=None, nombre_indicador=None, valor_consulta=None, cantidad=None, nombres_ids=None ):
    data_json_str = request.GET.get('data_json')
    data_json = json.loads(data_json_str) if data_json_str else None

    context = {
        'data': inegi_code,
        'name': nombre_indicador,
        'valor_consulta': valor_consulta,
        'canitdad': cantidad,
        'nombres': nombres_ids
    }
    return render(request, 'prueba_inegi.html', context)

def corrida_financiera(request):
    #////////////////////////////////////
    #Definicion de diccionarios
    memorias_calculo = {'ventas_semana': []}
    salarios = {'salarios': [],
                'importe_mensual':[]}
    servicios_mantto = {}
    costo_proyecto1_mensual = {}

    #Definicion de variables
    B2_Memorias_calculo_Total_venta_semana = [sum(memorias_calculo['ventas_semana'])]
    B2_Salarios_Total_Sueldo_Mensual =  [sum(salarios['sueldo_mensual'])]
    B2_Servicios_Total_Mensual = [sum(salarios['importe_mensual'])]
    B2_Servicios_Mantto_Mensual_Total = [sum(servicios_mantto['importe_mensual'])]
    B2_Costo_Materiales_Por_Dia = []
    B3_Costo_Proyecto1_Mensual_Por_Dia = []

    unidad_value = ''
    cantidad_value = 0

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//Definicion de diccionarios
    #BLOQUE 1: PRESUPUESTO DE INVERSION
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    activo_fijo = {'concepto': [],
                   'unidad': [],
                   'cantidad': [],
                   'costo_unitario': []}
    activo_fijo['montos'] = [costo_unitario * cantidad for costo_unitario, cantidad in
                              zip(activo_fijo['costo_unitario'], activo_fijo['cantidad'])]
    activo_fijo['programa'] = [activo_fijo['montos']]
    activo_fijo['socios'] = [activo_fijo['montos']]
    activo_fijo['total'] = [programa + socios for programa, socios in zip(activo_fijo['programa'],
                                                                        activo_fijo['socios'])]



    Activo_diferido = {'concepto': [],
                       'unidad': [],
                       'cantidad':[],
                       'consumo_unitario': []}
    # Calculamos el monto multiplicando cantidad por consumo_unitario
    Activo_diferido['montos'] = [cantidad * consumo_unitario for cantidad, consumo_unitario in
                                 zip(Activo_diferido['cantidad'], Activo_diferido['consumo_unitario'])]
    # Asignamos el valor de montos a programa y socios (no está claro si realmente deseas esto)
    Activo_diferido['programa'] = Activo_diferido['montos']
    Activo_diferido['socios'] = Activo_diferido['montos']
    # Calculamos el total sumando programa y socios
    Activo_diferido['total'] = [programa + socio for programa, socio in
                                zip(Activo_diferido['programa'], Activo_diferido['socios'])]


    #NOTA: Se elimina diccionario 'capital_trabajo_servicio'



    capital_trabajo_mano_obra = {'unidad':[],
                                 'cantidad':[],
                                 'costo_unitario': B2_Salarios_Total_Sueldo_Mensual}
    capital_trabajo_mano_obra['montos'] = [costo_unitario * cantidad for costo_unitario, cantidad in
                                           zip(capital_trabajo_mano_obra['costo_unitario'],
                                               capital_trabajo_mano_obra['cantidad'])]
    capital_trabajo_mano_obra['programa'] = [capital_trabajo_mano_obra['montos']]
    capital_trabajo_mano_obra['socios'] = [capital_trabajo_mano_obra['montos']]
    capital_trabajo_mano_obra['total'] = [sum(capital_trabajo_mano_obra['programa']
                                           + capital_trabajo_mano_obra['socios'])]



    capital_trabajo_servicios ={'unidad': [],
                                'cantidad': [],
                                'costo_unitario': B2_Servicios_Total_Mensual}
    capital_trabajo_servicios['montos'] = [costo_unitario * cantidad for costo_unitario, cantidad in
                                         zip(capital_trabajo_servicios['costo_unitario'],
                                             capital_trabajo_servicios['cantidad'])]
    capital_trabajo_servicios['programa'] = [capital_trabajo_servicios['montos']]
    capital_trabajo_servicios['socios'] = [capital_trabajo_servicios['montos']]
    capital_trabajo_servicios['total'] = [sum(capital_trabajo_servicios['programa']
                                           + capital_trabajo_servicios['socios'])]



    capital_trabajo_servicios_mantto={'unidad':[],
                                      'cantidad':[],
                                      'costo_unitario':B2_Servicios_Mantto_Mensual_Total}
    capital_trabajo_servicios_mantto['montos'] = [costo_unitario * cantidad for costo_unitario, cantidad in
                                                  zip(capital_trabajo_servicios_mantto['costo_unitario'],
                                                      capital_trabajo_servicios_mantto['cantidad'])]
    capital_trabajo_servicios_mantto['programa'] = [capital_trabajo_servicios_mantto['montos']]
    capital_trabajo_servicios_mantto['socios'] = [capital_trabajo_servicios_mantto['montos']]
    capital_trabajo_servicios_mantto['total'] = [sum(capital_trabajo_servicios_mantto['programas']
                                                  + capital_trabajo_servicios_mantto['socios'])]


    total_presupuesto_inversion={'total_monto':sum(capital_trabajo_servicios['montos']
                                 + capital_trabajo_mano_obra['montos']+capital_trabajo_servicios_mantto['montos']
                                 + activo_fijo['montos']+Activo_diferido['montos']),

                                 'total_programa': sum(capital_trabajo_servicios['programa']
                                 + capital_trabajo_mano_obra['programa']+ capital_trabajo_servicios_mantto['programa']
                                 + activo_fijo['programa']+Activo_diferido['programa']),

                                 'total_socios': sum(capital_trabajo_servicios['socios']
                                 + capital_trabajo_mano_obra['socios']+capital_trabajo_servicios_mantto['socios']
                                 + activo_fijo['socios']+Activo_diferido['socios']),
                                 }
    total_presupuesto_inversion={'total_B1': sum(total_presupuesto_inversion['total_programa']
                                 + total_presupuesto_inversion['total_socios'])}

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # BLOQUE 2: MEMORIAS DE CALCULO
    #///////////////////////////////
    #Deficicion de diccionarios

    #Definicion de variables

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    memorias_calculo = {'concepto': [],
                        'presentacion': [],
                        'costo_insumo': [B2_Costo_Materiales_Por_Dia],
                        'ventas_semana': []}
    memorias_calculo['costo_semanal'] = [costo_insumo * ventas_semana for costo_insumo, ventas_semana in zip(
                                        memorias_calculo['costo_insumo'], memorias_calculo['ventas_semana'])]
    memorias_calculo['costo_mensual'] = [costo_semanal * 4 for costo_semanal in memorias_calculo['ventas_semana']]
    memorias_calculo['precio_venta'] = [costo_insumo * 1.35 for costo_insumo in memorias_calculo['costo_insumo']]
    memorias_calculo['ingreso_semanal'] = [precio_venta * ventas_semana for precio_venta, ventas_semana in
                                           zip(memorias_calculo['precio_venta'], memorias_calculo['ventas_semana'])]
    memorias_calculo['ingreso_mensual'] = [ingreso_semanal * 4 for ingreso_semanal in memorias_calculo['ingreso_semanal']]
    memorias_calculo['ingreso_anual'] = [ingreso_mensual * 12 for ingreso_mensual in memorias_calculo['ingreso_mensual']]
    memorias_calculo['total_ventas_semana'] = [sum(memorias_calculo['ventas_semana'])]
    memorias_calculo['total_costo_semana'] = [sum(memorias_calculo['costo_semanal'])]
    memorias_calculo['total_costo_mensual'] = [sum(memorias_calculo['costo_mensual'])]
    memorias_calculo['total_ingreso_semanal'] = [sum(memorias_calculo['ingreso_semanal'])]
    memorias_calculo['total_ingreso_mensual'] = [sum(memorias_calculo['ingreso_mensual'])]
    memorias_calculo['total_ingreso_anual'] = [sum(memorias_calculo['ingreso_anual'])]
    memorias_calculo['ganacia_semanal'] = [total_ingreso_semanal - total_costo_semana
                                           for total_ingreso_semanal, total_costo_semana in
                                           zip(memorias_calculo['total_ingreso_semanal'],
                                               memorias_calculo['total_costo_semana'])]
    memorias_calculo['ganancia_mensual'] = [ganancia_semanal * 4 for ganancia_semanal in memorias_calculo['ganacia_semanal']]
    memorias_calculo['ganancia_anual'] = [ganancia_mensual * 12 for ganancia_mensual in memorias_calculo['ganancia_mensual']]




    registro_propiedad_intelectual = {'concepto': [],
                                      'cantidad': [],
                                      'precio_unitario': []}
    registro_propiedad_intelectual['precio_total'] = [cantidad * precio_unitario for cantidad, precio_unitario
                                                      in zip(registro_propiedad_intelectual['cantidad'],
                                                             registro_propiedad_intelectual['precio_unitario'])]
    registro_propiedad_intelectual['total'] = [sum(registro_propiedad_intelectual['precio_total'])]




    servicios_administrativos = {'concepto': [],
                                 'cantidad': [],
                                 'precio_unitario': []}
    servicios_administrativos['precio_total'] = [cantidad * precio_unitario for cantidad, precio_unitario
                                                 in zip(servicios_administrativos['cantidad'],
                                                        servicios_administrativos['precio_unitario'])]
    servicios_administrativos['total'] = [sum(servicios_administrativos['precio_total'])]




    servicios = {'concepto': [],
                 'importe_mensual': []}
    servicios['importe_2meses'] = [importe_mensual * 2 for importe_mensual in zip(servicios['importe_mensual'])]
    servicios['importe_anual'] = [importe_anual * 12 for importe_anual in zip(servicios['importe_mensual'])]
    servicios['mensual_total'] = [sum(servicios['importe_mensual'])]
    servicios['anual_total'] = [sum(servicios['importe_anual'])]




    servicios_mantto={'concepto': [],
                      'importe_mensual': []}
    servicios_mantto['importe_2meses'] = [importe_mensual * 2 for importe_mensual
                                          in servicios_mantto['importe_mensual']]
    servicios_mantto['importe_anual'] = [importe_anual * 12 for importe_anual
                                         in servicios_mantto['importe_mensual']]
    servicios_mantto['mensual_total'] = [sum(servicios_mantto['importe_mensual'])]
    servicios_mantto['anual_total'] = [sum(servicios_mantto['importe_anual'])]




    salarios = {'puesto': [],
                'cantidad': [],
                'sueldo_mensual': []}
    salarios['sueldo_diario'] = [sueldo_diario / 30 for sueldo_diario
                                 in salarios['sueldo_mensual']]
    salarios['sueldo_anual'] = [sueldo_anual * 12 for sueldo_anual
                                in salarios['sueldo_mensual']]
    salarios['total_sueldo_mensual'] = [sum(salarios['sueldo_mensual'])]
    salarios['total_sueldo_anual'] = [sum(salarios['sueldo_anual'])]




    #/////////////////////////////////////////////////////////////
    costo_proyecto1_mensual = {'costo_mensual': [sum(servicios['importe_mensual']+salarios['sueldo_mensual']
                                                     + servicios_administrativos['precio_unitario'])
                                                + servicios_mantto['mensual_total']]}
    #////////////////////////////////////////////////////////////
    costo_materiales = {'materiales': [],
                        'unidad': []}
    costo_materiales['por_dia'] =[costo_proyecto1_mensual['costo_mensual'] / 30]

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # BLOQUE 3: PROYECCION DE COSTOS
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    costos_proyecto1 = {'concepto': [concepto for concepto in servicios['concepto']],
                        'costo_mensual': [importe_mensual for importe_mensual in servicios['importe_mensual']]}
    costos_proyecto1['año1'] = [costo_mensual * 12 for costo_mensual in costos_proyecto1['costo_mensual']]
    costos_proyecto1['año2'] = [año1 * 1.02 for año1 in costos_proyecto1['año1']]
    costos_proyecto1['año3'] = [año2 * 1.02 for año2 in costos_proyecto1['año2']]
    costos_proyecto1['año4'] = [año3 * 1.02 for año3 in costos_proyecto1['año3']]
    costos_proyecto1['año5'] = [año4 * 1.02 for año4 in costos_proyecto1['año4']]




    costos_proyecto2 = {'concepto': [concepto for concepto in memorias_calculo['concepto']],
                        'costo_mensual': [costo_mensual for costo_mensual in memorias_calculo['costo_mensual']]}
    costos_proyecto2['año1'] = [costo_mensual * 12 for costo_mensual in costos_proyecto2['costo_mensual']]
    costos_proyecto2['año2'] = [año1 * 1.02 for año1 in costos_proyecto2['año1']]
    costos_proyecto2['año3'] = [año2 * 1.02 for año2 in costos_proyecto2['año2']]
    costos_proyecto2['año4'] = [año3 * 1.02 for año3 in costos_proyecto2['año3']]
    costos_proyecto2['año5'] = [año4 * 1.02 for año4 in costos_proyecto2['año4']]



    totales = {'total_costo_mensual': [sum(costos_proyecto1['costo_mensual'] + costos_proyecto2['costo_mensual'])],
               'total_año1': [sum(costos_proyecto1['año1'] + costos_proyecto2['año1'])],
               'total_año2': [sum(costos_proyecto1['año2'] + costos_proyecto2['año2'])],
               'total_año3': [sum(costos_proyecto1['año3'] + costos_proyecto2['año3'])],
               'total_año4': [sum(costos_proyecto1['año4'] + costos_proyecto2['año4'])],
               'total_año5': [sum(costos_proyecto1['año5'] + costos_proyecto2['año5'])]}




    costo_proyecto1_mensual['costo_dia'] = [costo_proyecto1_mensual['costo_mensual'] / 30]

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # BLOQUE 4: COSTOS TOTALES
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    costos_fijos = {'concepto': [concepto for concepto in costos_proyecto1['concepto']],
                    'año1': [año1 for año1 in costos_proyecto1['año1']],
                    'año2': [año2 for año2 in costos_proyecto1['año2']],
                    'año3': [año3 for año3 in costos_proyecto1['año3']],
                    'año4': [año4 for año4 in costos_proyecto1['año4']],
                    'año5': [año5 for año5 in costos_proyecto1['año5']]}
    costos_fijos['total_año1'] = [sum(costos_fijos['año1'])]
    costos_fijos['total_año2'] = [sum(costos_fijos['año2'])]
    costos_fijos['total_año3'] = [sum(costos_fijos['año3'])]
    costos_fijos['total_año4'] = [sum(costos_fijos['año4'])]
    costos_fijos['total_año5'] = [sum(costos_fijos['año5'])]



    costos_variables = {'concepto': [concepto for concepto in costos_proyecto2['concepto']],
                        'año1': [año1 for año1 in costos_proyecto2['año1']],
                        'año2': [año2 for año2 in costos_proyecto2['año2']],
                        'año3': [año3 for año3 in costos_proyecto2['año3']],
                        'año4': [año4 for año4 in costos_proyecto2['año4']],
                        'año5': [año5 for año5 in costos_proyecto2['año5']]}
    costos_variables['total_año1'] = [sum(costos_variables['año1'])]
    costos_variables['total_año2'] = [sum(costos_variables['año2'])]
    costos_variables['total_año3'] = [sum(costos_variables['año3'])]
    costos_variables['total_año4'] = [sum(costos_variables['año4'])]
    costos_variables['total_año5'] = [sum(costos_variables['año5'])]




    costos_totales = {'costo_fijo_año1': [total_año1 for total_año1 in costos_fijos['total_año1']],
                      'costo_fijo_año2': [total_año2 for total_año2 in costos_fijos['total_año2']],
                      'costo_fijo_año3': [total_año3 for total_año3 in costos_fijos['total_año3']],
                      'costo_fijo_año4': [total_año4 for total_año4 in costos_fijos['total_año4']],
                      'costo_fijo_año5': [total_año5 for total_año5 in costos_fijos['total_año5']],
                      'costo_variable_año1': [total_año1 for total_año1 in costos_variables['total_año1']],
                      'costo_variable_año2': [total_año2 for total_año2 in costos_variables['total_año2']],
                      'costo_variable_año3': [total_año3 for total_año3 in costos_variables['total_año3']],
                      'costo_variable_año4': [total_año4 for total_año4 in costos_variables['total_año4']],
                      'costo_variable_año5': [total_año5 for total_año5 in costos_variables['total_año5']]}
    costos_totales['costos_totales_año1'] = [sum(costos_totales['costo_fijo_año1'] + costos_totales['costo_variable_año1'])]
    costos_totales['costos_totales_año2'] = [sum(costos_totales['costo_fijo_año2'] + costos_totales['costo_variable_año2'])]
    costos_totales['costos_totales_año3'] = [sum(costos_totales['costo_fijo_año3'] + costos_totales['costo_variable_año3'])]
    costos_totales['costos_totales_año4'] = [sum(costos_totales['costo_fijo_año4'] + costos_totales['costo_variable_año4'])]
    costos_totales['costos_totales_año5'] = [sum(costos_totales['costo_fijo_año5'] + costos_totales['costo_variable_año5'])]

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # BLOQUE 5: PROYECCIÓN DE INGRESOS
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    proyeccion_ingresos = {'concepto': [concepto for concepto in memorias_calculo['concepto']],
                           'volumen_venta_mensual': [ventas_semana * 4 for ventas_semana
                                                     in memorias_calculo['ventas_semana']],
                           'precio_unitario': [precio_venta for precio_venta
                                               in memorias_calculo['precio_venta']]}
    proyeccion_ingresos['ventas_mensual'] = [precio_unitario * volumen_venta_mensual
                                             for precio_unitario, volumen_venta_mensual
                                             in zip(proyeccion_ingresos['precio_unitario'],
                                                    proyeccion_ingresos['volumen_venta_mensual'])]
    proyeccion_ingresos['año1'] = [ventas_mensual * 12 for ventas_mensual
                                   in proyeccion_ingresos['ventas_mensual']]
    proyeccion_ingresos['año2'] = [año1 * 1.05 for año1
                                   in proyeccion_ingresos['año1']]
    proyeccion_ingresos['año3'] = [año2 * 1.05 for año2
                                   in proyeccion_ingresos['año2']]
    proyeccion_ingresos['año4'] = [año3 * 1.05 for año3
                                   in proyeccion_ingresos['año3']]
    proyeccion_ingresos['año5'] = [año4 * 1.05 for año4
                                   in proyeccion_ingresos['año4']]
    proyeccion_ingresos['total_ventas_mensual'] = [sum(proyeccion_ingresos['ventas_mensual'])]
    proyeccion_ingresos['total_año1'] = [sum(proyeccion_ingresos['año1'])]
    proyeccion_ingresos['total_año2'] = [sum(proyeccion_ingresos['año2'])]
    proyeccion_ingresos['total_año3'] = [sum(proyeccion_ingresos['año3'])]
    proyeccion_ingresos['total_año4'] = [sum(proyeccion_ingresos['año4'])]
    proyeccion_ingresos['total_año5'] = [sum(proyeccion_ingresos['año5'])]

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # BLOQUE 6: ESTADO DE RESULTADOS
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    costos_depreciaciones = {'activi_fijo': [concepto for concepto in
                                             activo_fijo['concepto']],
                             'valor_original': [montos for montos in
                                                activo_fijo['montos']],
                             'tasa': 0.10,
                             'años': 5}
    costos_depreciaciones['depreciacion_anual'] = [valor_original * costos_depreciaciones['tasa']
                                                   for valor_original, tasa
                                                   in costos_depreciaciones['valor_original']]
    costos_depreciaciones['valor_rescate'] = [valor_original - (depreciacion_anual * costos_depreciaciones['años'])
                                              for valor_original, depreciacion_anual
                                              in zip(costos_depreciaciones['valor_original'],
                                                     costos_depreciaciones['depreciacion_anual'])]
    costos_depreciaciones['total_valor_original'] = [sum(costos_depreciaciones['valor_original'])]
    costos_depreciaciones['total_depreciacion_anual'] = [sum(costos_depreciaciones['depreciacion_anual'])]
    costos_depreciaciones['total_valor_rescate'] = sum(costos_depreciaciones['valor_rescate'])



    estado_resultados = {'ventas_año1': [total_ventas_año1 for total_ventas_año1
                                         in proyeccion_ingresos['total_año1']],
                         'ventas_año2': [total_ventas_año2 for total_ventas_año2
                                         in proyeccion_ingresos['total_año2']],
                         'ventas_año3': [total_ventas_año3 for total_ventas_año3
                                         in proyeccion_ingresos['total_año3']],
                         'ventas_año4': [total_ventas_año4 for total_ventas_año4
                                         in proyeccion_ingresos['total_año4']],
                         'ventas_año5': [total_ventas_año5 for total_ventas_año5
                                        in proyeccion_ingresos['total_año5']],
                         'costos_fijos_año1': [total_costos_año1 for total_costos_año1
                                         in costos_fijos['total_año1']],
                         'costos_fijos_año2': [total_costos_año2 for total_costos_año2
                                         in costos_fijos['total_año2']],
                         'costos_fijos_año3': [total_costos_año3 for total_costos_año3
                                         in costos_fijos['total_año3']],
                         'costos_fijos_año4': [total_costos_año4 for total_costos_año4
                                         in costos_fijos['total_año4']],
                         'costos_fijos_año5': [total_costos_año5 for total_costos_año5
                                         in costos_fijos['total_año5']],
                         'costos_variables_año1': [costos_variables_año1 for costos_variables_año1
                                                   in costos_variables['total_año1']],
                         'costos_variables_año2': [costos_variables_año2 for costos_variables_año2
                                                   in costos_variables['total_año2']],
                         'costos_variables_año3': [costos_variables_año3 for costos_variables_año3
                                                   in costos_variables['total_año3']],
                         'costos_variables_año4': [costos_variables_año4 for costos_variables_año4
                                                   in costos_variables['total_año4']],
                         'costos_variables_año5': [costos_variables_año5 for costos_variables_año5
                                                   in costos_variables['total_año5']]}
    estado_resultados['costos_totales_año1'] = [costos_fijos_año1 + costos_variables_año1
                                                 for costos_fijos_año1, costos_variables_año1
                                                 in zip(estado_resultados['costos_fijos_año1'],
                                                        estado_resultados['costos_variables_año1'])]
    estado_resultados['costos_totales_año2'] = [costos_fijos_año2 + costos_variables_año2
                                                for costos_fijos_año2, costos_variables_año2
                                                in zip(estado_resultados['costos_fijos_año2'],
                                                       estado_resultados['costos_variables_año2'])]
    estado_resultados['costos_totales_año3'] = [costos_fijos_año3 + costos_variables_año3
                                                for costos_fijos_año3, costos_variables_año3
                                                in zip(estado_resultados['costos_fijos_año3'],
                                                       estado_resultados['costos_variables_año3'])]
    estado_resultados['costos_totales_año4'] = [costos_fijos_año4 + costos_varibales_año4
                                                for costos_fijos_año4, costos_varibales_año4
                                                in zip(estado_resultados['costos_fijos_año4'],
                                                        estado_resultados['costos_variables_año4'])]
    estado_resultados['costos_totales_año5'] = [costos_fijos_año5 + costos_variables_año5
                                                for costos_fijos_año5, costos_variables_año5
                                                in zip(estado_resultados['costos_fijos_año5'])]
    estado_resultados['utilidad_bruta_año1'] = [ventas_año1 - costos_totales_año1
                                                for ventas_año1, costos_totales_año1
                                                in zip(estado_resultados['ventas_año1'],
                                                       estado_resultados['costos_totales_año1'])]
    estado_resultados['utilidad_bruta_año2'] = [ventas_año2 - costos_totales_año2
                                                for ventas_año2, costos_totales_año2
                                                in zip(estado_resultados['ventas_año2'],
                                                       estado_resultados['costos_totales_año2'])]
    estado_resultados['utilidad_bruta_año3'] = [ventas_año3 - costos_totales_año3
                                                for ventas_año3, costos_totales_año3
                                                in zip(estado_resultados['ventas_año3'],
                                                       estado_resultados['costos_totales_año3'])]
    estado_resultados['utilidad_bruta_año4'] = [ventas_año4 - costos_totales_año4
                                                for ventas_año4, costos_totales_año4
                                                in zip(estado_resultados['ventas_año4'],
                                                       estado_resultados['costos_totales_año4'])]
    estado_resultados['utilidad_bruta_año5'] = [ventas_año5 - costos_totales_año5
                                                for ventas_año5, costos_totales_año5
                                                in zip(estado_resultados['ventas_año5'],
                                                       estado_resultados['costos_totales_año5'])]
    estado_resultados['depreciacion_año1'] = [total_depreciacion_anual for total_depreciacion_anual
                                              in costos_depreciaciones['total_depreciacion_anual']]
    estado_resultados['depreciacion_año2'] = [depreciacion_año1 * 1.05 for depreciacion_año1
                                              in estado_resultados['depreciacion_año1']]
    estado_resultados['depreciacion_año3'] = [depreciacion_año2 * 1.05 for depreciacion_año2
                                              in estado_resultados['depreciacion_año2']]
    estado_resultados['depreciacion_año4'] = [depreciacion_año3 * 1.05 for depreciacion_año3
                                              in estado_resultados['depreciacion_año3']]
    estado_resultados['depreciacion_año5'] = [depreciacion_año4 * 1.05 for depreciacion_año4
                                              in estado_resultados['depreciacion_año4']]
    estado_resultados['utilidad_antes_impuestos_año1'] = [utilidad_bruta_año1 - depreciacion_año1
                                                          for utilidad_bruta_año1, depreciacion_año1
                                                          in zip(estado_resultados['utilidad_bruta_año1'],
                                                                 estado_resultados['depreciacion_año1'])]
    estado_resultados['utilidad_antes_impuestos_año2'] = [utilidad_bruta_año2 - depreciacion_año2
                                                          for utilidad_bruta_año2, depreciacion_año2
                                                          in zip(estado_resultados['utilidad_bruta_año2'],
                                                                 estado_resultados['depreciacion_año2'])]
    estado_resultados['utilidad_antes_impuestos_año3'] = [utilidad_bruta_año3 - depreciacion_año3
                                                          for utilidad_bruta_año3, depreciacion_año3
                                                          in zip(estado_resultados['utilidad_bruta_año3'],
                                                                 estado_resultados['depreciacion_año3'])]
    estado_resultados['utilidad_antes_impuestos_año4'] = [utilidad_bruta_año4 - depreciacion_año4
                                                          for utilidad_bruta_año4, depreciacion_año4
                                                          in zip(estado_resultados['utilidad_bruta_año4'],
                                                                 estado_resultados['depreciaion_año4'])]
    estado_resultados['utilidad_antes_impuestos_año5'] = [utilidad_bruta_año5 - depreciacion_año5
                                                          for utilidad_bruta_año5, depreciacion_año5
                                                          in zip(estado_resultados['utilidad_bruta_año5'],
                                                                 estado_resultados['depreciacion_año5'])]
    estado_resultados['impuestos_año1'] = [utilidad_antes_impuestos_año1 * costos_depreciaciones['tasa']
                                           for utilidad_antes_impuestos_año1
                                           in estado_resultados['utilidad_antes_impuestos_año1']]
    estado_resultados['impuestos_año2'] = [utilidad_antes_impuestos_año2 * costos_depreciaciones['tasa']
                                           for utilidad_antes_impuestos_año2
                                           in estado_resultados['utiliddad_antes_impuestos_año2']]
    estado_resultados['impuestos_año3'] = [utilidad_antes_impuestos_año3 * costos_depreciaciones['tasa']
                                           for utilidad_antes_impuestos_año3
                                           in estado_resultados['utilidad_antes_impuestos_año3']]
    estado_resultados['impuestos_año4'] = [utilidad_antes_impuestos_año4 * costos_depreciaciones['tasa']
                                           for utilidad_antes_impuestos_año4
                                           in estado_resultados['utilidad_antes_impuestos_año4']]
    estado_resultados['impuestos_año5'] = [utilidad_antes_impuestos_año5 * costos_depreciaciones['tasa']
                                           for utilidad_antes_impuestos_año5
                                           in estado_resultados['utilidad_antes_impuestos_año5']]
    estado_resultados['utilidad_ejercicio_año1'] = [utilidad_antes_impuestos_año1 - impuestos_año1
                                                    for utilidad_antes_impuestos_año1, impuestos_año1
                                                    in zip(estado_resultados['utilidad_antes_impuestos_año1'],
                                                           estado_resultados['impuestos_año1'])]
    estado_resultados['utilidad_ejercicio_año2'] = [utilidad_antes_impuestos_año2 - impuestos_año2
                                                    for utilidad_antes_impuestos_año2, impuestos_año2
                                                    in zip(estado_resultados['utilidad_antes_impuestos_año2'],
                                                           estado_resultados['impuestos_año2'])]
    estado_resultados['utilidad_ejercicio_año3'] = [utilidad_antes_impuestos_año3 - impuestos_año3
                                                    for utilidad_antes_impuestos_año3, impuestos_año3
                                                    in zip(estado_resultados['utilidad_antes_impuestos_año3'],
                                                           estado_resultados['impuestos_año3'])]
    estado_resultados['utilidad_ejercicio_año4'] = [utilidad_antes_impuestos_año4 - impuestos_año4
                                                    for utilidad_antes_impuestos_año4, impuestos_año4
                                                    in zip(estado_resultados['utilidad_antes_impuestos_año4'],
                                                           estado_resultados['impuestos_año4'])]
    estado_resultados['utilidad_ejercicio_año5'] = [utilidad_antes_impuestos_año5 - impuestos_año5
                                                    for utilidad_antes_impuestos_año5, impuestos_año5
                                                    in zip(estado_resultados['utilidad_antes_impuestos_año5'],
                                                           estado_resultados['impuestos_año5'])]

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # BLOQUE : FLUJO DE EFECTIVO
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    flujo_efectivo = {'ventas_año1': [total_año1 for total_año1
                                      in proyeccion_ingresos['total_año1']],
                      'ventas_año2': [total_año2 for total_año2
                                      in proyeccion_ingresos['total_año2']],
                      'ventas_año3': [total_año3 for total_año3
                                      in proyeccion_ingresos['total_año3']],
                      'ventas_año4': [total_año4 for total_año4
                                      in proyeccion_ingresos['total_año4']],
                      'ventas_año5': [total_año5 for total_año5
                                      in proyeccion_ingresos['total_año5']],
                      'valor_rescate': costos_depreciaciones['total_valor_rescate']}
    flujo_efectivo['ingresos_totales_año1'] = [ventas_año1 for ventas_año1
                                               in flujo_efectivo['ventas_año1']]
    flujo_efectivo['ingresos_totales_año2'] = [ventas_año2 for ventas_año2
                                               in flujo_efectivo['ventas_año2']]
    flujo_efectivo['ingresos_totales_año3'] = [ventas_año3 for ventas_año3
                                               in flujo_efectivo['ventas_año3']]
    flujo_efectivo['ingresos_totales_año4'] = [ventas_año4 for ventas_año4
                                               in flujo_efectivo['ventas_año4']]
    flujo_efectivo['ingresos_totales_año5'] = [ventas_año5 + valor_rescate
                                               for ventas_año5, valor_rescate
                                               in zip(flujo_efectivo['ventas_año5'],
                                                      flujo_efectivo['valor_rescate'])]
    #pendiente continuar diccionario flujo_efectivo
    #xd

    return render(request, 'prueba_inegi.html')