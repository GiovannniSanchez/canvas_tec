from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import answers_user, AnswersChatgpt, GeneratedImage, LogoProyect,data_corrida_financiera
from .forms import RegisterAnswer, LoadLogo
import openai
import requests
import json
from fuzzywuzzy import fuzz
from urllib.parse import urlencode
from django.urls import reverse
import time


def about(request):
    return render(request, 'about.html')

@login_required
def prueba(request):
    user = request.user

    last = answers_user.objects.filter(user=user).last()

    # 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
    openai.api_key = "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"

    # Contexto del asistente
    messages = [{"role": "system", "content": "Eres un experto en modelos de negocio"}]

    segmento = ' ¿Para quiénes son tus productos o servicios? ¿Cómo son esas personas u organizaciones?: ', last.segmento
    propuesta = ' ¿Qué problema resuelves o qué necesidad cubres para tus clientes?: ', last.propuesta
    canales = ' ¿Cómo llegarán tus productos o servicios a tus clientes? ¿Cómo los encontrarán?: ', last.canales
    relaciones = ' ¿Cómo te relacionarás con tus clientes? ¿Cómo los tratarás?: ', last.relaciones
    recursos = ' ¿Qué cosas necesitas para hacer que tu proyecto funcione? ¿Qué es esencial?: ', last.recursos
    actividades = '¿Qué cosas tendrás que hacer todos los días para que tu proyecto funcione bien?: ', last.actividades
    socios = ' ¿Trabajarás con otras personas o empresas en tu proyecto?: ', last.socios

    prompt_default = 'Tomando en cuenta la estructura del modelo canvas '

    prompt_default1 = 'puedes darme el "Segmento de clientes" segun tu interpretacion como experto en modelo de negocios ' \
                      'haciendo referencia a '+ str(segmento)+' , con un maximo de 40 palabras, unicamente en forma de lista y sin repetir la pregunta '

    prompt_default2 = 'puedes darme la "Propuesta de valor" segun tu interpretacion como experto en modelo de negocios' \
                      'haciendo referencia a '+str(propuesta)+', con un maximo de 40 palabras, unicamente en forma de lista y sin repetir la pregunta'

    prompt_default3 = 'puedes darme los "Canales de distribución" segun tu interpretacion como experto en modelo de negocios' \
                      'haciendo referencia a ' +str(canales) +', con un maximo de 40 palabras, unicamente en forma de lista y sin repetir la pregunta'

    prompt_default4 = 'puedes darme las "Relaciones con los clientes" segun tu interpretacion como experto en modelo de negocios' \
                      'haciendo referencia a '+str(relaciones)+', con un maximo de 40 palabras, unicamente en forma de lista y sin repetir la pregunta'

    prompt_default5 = 'puedes darme los "Recursos clave" segun tu interpretacion como experto en modelo de negocios' \
                      'haciendo referencia a '+str(recursos) +', con un maximo de 40 palabras, unicamente en forma de lista y sin repetir la pregunta'

    prompt_default6 = ' puedes darme las "Actividades clave" segun tu interpretacion como experto en modelo de negocios' \
                      ' haciendo referencia a '+str(actividades)+', con un maximo de 40 palabras, unicamente en forma de lista y sin repetir la pregunta'

    prompt_default7 = ' puedes darme los "Socios clave" segun tu interpretacion como experto en modelo de negocios' \
                      ' haciendo referencia a '+str(socios) +', con un maximo de 40 palabras, unicamente en forma de lista y sin repetir la pregunta'



    # ////////////////////////////////////////////////////////////////////////////////////////
    contenido = prompt_default + prompt_default1
    messages.append({"role": "user", "content": contenido})
    respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=messages, max_tokens=300)
    respuesta_segmento = respuesta.choices[0].message.content
    time.sleep(5)
    # ///////////////////////////////////////////////////////////////////////////////////////////
    contenido1 = prompt_default + prompt_default2
    messages.append({"role": "user", "content": contenido1})
    respuesta1 = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=messages, max_tokens=300)
    respuesta_propuesta = respuesta1.choices[0].message.content
    time.sleep(5)
    # ////////////////////////////////////////////////////////////////////////////////////////////////////
    contenido2 = prompt_default + prompt_default3

    messages.append({"role": "user", "content": contenido2})
    respuesta2 = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=messages, max_tokens=300)
    respuesta_canales = respuesta2.choices[0].message.content
    time.sleep(5)
    #
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////
    contenido3 = prompt_default + prompt_default4

    messages.append({"role": "user", "content": contenido3})
    respuesta3 = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=messages, max_tokens=300)
    respuesta_relaciones = respuesta3.choices[0].message.content
    time.sleep(5)
    # /////////////////////////////////////////////////////////////////////////////////////////////////////7
    contenido4 = prompt_default + prompt_default5

    messages.append({"role": "user", "content": contenido4})
    respuesta4 = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=messages, max_tokens=300)
    respuesta_recursos = respuesta4.choices[0].message.content
    time.sleep(5)
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////
    contenido5 = prompt_default + prompt_default6

    messages.append({"role": "user", "content": contenido5})
    respuesta5 = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=messages, max_tokens=300)
    respuesta_actividades = respuesta5.choices[0].message.content
    time.sleep(5)
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////
    contenido6 = prompt_default + prompt_default7

    messages.append({"role": "user", "content": contenido6})
    respuesta6 = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=messages, max_tokens=300)
    respuesta_socios = respuesta6.choices[0].message.content
    time.sleep(5)
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////
    #GENERACION DE PROMPT PARA IMAGENES
    palabras_clave = [respuesta_segmento, respuesta_segmento, respuesta_propuesta,
                      respuesta_propuesta, respuesta_canales, respuesta_relaciones, respuesta_recursos,
                      respuesta_actividades, respuesta_socios, respuesta_socios, 'genera una imagen de una mano recibiendo dinero',
                      'genera una imagen representativa de costos de empresa']

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////
    #GENERACIÓN DE IMAGENES

    urls_images = []

    for prompt in palabras_clave:
        response = openai.Image.create(
            prompt=prompt + 'sin texto grande',
            n=1,
            size = "256x256"
        )
        time.sleep(5)
        urls_images.append(response['data'][0]['url'])


    # Guardar la respuesta en la base de datos
    answer_chat = AnswersChatgpt.objects.create(user=user,
                                                segmento_gpt=respuesta_segmento,
                                                propuesta_gpt=respuesta_propuesta,
                                                canales_gpt=respuesta_canales,
                                                relaciones_gpt=respuesta_relaciones,
                                                recursos_gpt=respuesta_recursos,
                                                actividades_gpt=respuesta_actividades,
                                                socios_gpt=respuesta_socios
                                                )
    answer_chat.save()
    #Guardar las urls de imagenes en la base de datos
    images_save = GeneratedImage.objects.create(user=user,
                                                segmento_image1=urls_images[0],
                                                segmento_image2=urls_images[1],
                                                propuesta_image1=urls_images[2],
                                                propuesta_image2=urls_images[3],
                                                canales_image=urls_images[4],
                                                relaciones_image=urls_images[5],
                                                recursos_image=urls_images[6],
                                                actividades_image=urls_images[7],
                                                socios_image1=urls_images[8],
                                                socios_image2=urls_images[9],
                                                ingresos_image=urls_images[10],
                                                costos_image=urls_images[11]
                                                )
    images_save.save()

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////

    return redirect('financiera')


@login_required
def formulario(request):
    if request.method == 'GET':
        data = {'form': RegisterAnswer(), 'logo_form': LoadLogo()}
        return render(request, 'formulario.html', data)
    else:

        user_id = request.user.id
        form = RegisterAnswer(request.POST)
        logo = LoadLogo(request.POST, request.FILES)
        if form.is_valid() and logo.is_valid():
            answers_user.objects.create(name_e_p=form.cleaned_data['name_e_p'],
                                        segmento=form.cleaned_data['segmento'],
                                        propuesta=form.cleaned_data['propuesta'],
                                        canales=form.cleaned_data['canales'],
                                        relaciones=form.cleaned_data['relaciones'],
                                        recursos=form.cleaned_data['recursos'],
                                        actividades=form.cleaned_data['actividades'],
                                        socios=form.cleaned_data['socios'],
                                         user_id=user_id)
            save_logo = LogoProyect.objects.create(user_id = user_id,
                                       logo = request.FILES['image'])
            save_logo.save()

            return redirect('Chatgpt')
        else:
            data = {'form': answers_user, 'logo_form': LoadLogo}
            return render(request, 'formulario.html', data)


@login_required
def test01(request):
    user = request.user
    answers = answers_user.objects.filter(user=user)
    return render(request, 'test01.html', {'respuestas': answers})


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
                nombre_indicador = item[
                    'Description']  # Asignar el valor de "Description" a la variable "nombre_indicador"
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

        # ///////////////////////////////////////////////////////////////////////////////////////////////////////
        # CONSULTA API DENUE
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
        # //////////////////////////////////////////////////////////////////////////////////////7
        params = urlencode(
            {'data_json': json.dumps(data_json)})  # Convertir a JSON y codificar como parámetro de consulta

        if inegi_code:
            url = reverse('resultado_inegi', kwargs={'inegi_code': indicador, 'nombre_indicador': nombre_indicador,
                                                     'valor_consulta': valor_consulta, 'cantidad': cantidad,
                                                     'nombres_ids': nombres_ids})
            return redirect(url)
        else:
            message = "Valor no encontrado"
            return redirect('resultado_inegi', inegi_code=message)


def resultado_inegi(request, inegi_code=None, nombre_indicador=None, valor_consulta=None, cantidad=None,
                    nombres_ids=None):
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
    if request.method == 'POST':
        user = request.user
        # //Definicion de diccionarios
        # BLOQUE 1: PRESUPUESTO DE INVERSION
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        activo_fijo = {'concepto': [],
                       'unidad': [],
                       'cantidad': [],
                       'costo_unitario': []}

        B1_Activo_fijo_concepto = request.POST.getlist('B1_activo_fijo_concepto')
        B1_Activo_fijo_unidad = request.POST.getlist('B1_activo_fijo_unidad')
        B1_Activo_fijo_cantidad = request.POST.getlist('B1_activo_fijo_cantidad')
        B1_Activo_fijo_precio_unitario = request.POST.getlist('B1_activo_fijo_precio_unitario')

        for B1_Activo_fijo_concepto, B1_Activo_fijo_unidad, B1_Activo_fijo_cantidad, B1_Activo_fijo_precio_unitario \
                in zip(B1_Activo_fijo_concepto, B1_Activo_fijo_unidad, B1_Activo_fijo_cantidad, B1_Activo_fijo_precio_unitario):
            activo_fijo['concepto'].append(B1_Activo_fijo_concepto)
            activo_fijo['unidad'].append(B1_Activo_fijo_unidad)
            activo_fijo['cantidad'].append(int(B1_Activo_fijo_cantidad))
            activo_fijo['costo_unitario'].append(float(B1_Activo_fijo_precio_unitario))

        activo_fijo['montos'] = [costo_unitario * cantidad for costo_unitario, cantidad in
                                 zip(activo_fijo['costo_unitario'], activo_fijo['cantidad'])]
        activo_fijo['programa'] = [montos for montos in activo_fijo['montos']]
        activo_fijo['socios'] = [montos for montos in activo_fijo['montos']]
        activo_fijo['total'] = [programa + socios for programa, socios in zip(activo_fijo['programa'],
                                                                              activo_fijo['socios'])]

        Activo_diferido = {'concepto': [],
                           'unidad': [],
                           'cantidad': [],
                           'costo_unitario': []}

        B1_Activo_diferido_concepto = request.POST.getlist('B1_activo_diferido_concepto')
        B1_Activo_diferido_unidad = request.POST.getlist('B1_activo_diferido_unidad')
        B1_Activo_diferido_cantidad = request.POST.getlist('B1_activo_diferido_cantidad')
        B1_Activo_diferido_precio_unitario = request.POST.getlist('B1_activo_diferido_precio_unitario')

        for B1_Activo_diferido_concepto, B1_Activo_diferido_unidad, B1_Activo_diferido_cantidad, B1_Activo_diferido_precio_unitario \
                in zip(B1_Activo_diferido_concepto, B1_Activo_diferido_unidad, B1_Activo_diferido_cantidad, B1_Activo_diferido_precio_unitario):
            Activo_diferido['concepto'].append(B1_Activo_diferido_concepto)
            Activo_diferido['unidad'].append(B1_Activo_diferido_unidad)
            Activo_diferido['cantidad'].append(int(B1_Activo_diferido_cantidad))
            Activo_diferido['costo_unitario'].append(float(B1_Activo_diferido_precio_unitario))
        print('xdddddddd')
        print(Activo_diferido['concepto'])
        print('Fijo', activo_fijo['concepto'])
        print('xdddddddd')
        # Calculamos el monto multiplicando cantidad por consumo_unitario
        Activo_diferido['montos'] = [cantidad * consumo_unitario for cantidad, consumo_unitario in
                                     zip(Activo_diferido['cantidad'], Activo_diferido['costo_unitario'])]
        # Asignamos el valor de montos a programa y socios (no está claro si realmente deseas esto)
        Activo_diferido['programa'] = [montos for montos in Activo_diferido['montos']]
        Activo_diferido['socios'] = [montos for montos in Activo_diferido['montos']]
        # Calculamos el total sumando programa y socios
        Activo_diferido['total'] = [programa + socio for programa, socio in
                                    zip(Activo_diferido['programa'], Activo_diferido['socios'])]

        # NOTA: Se elimina diccionario 'capital_trabajo_servicio'

        #//////////////////////////////////////////////////////////////////////////////////////////7
        #BLOQUE 2 : SALARIOS
        salarios = {'puesto': [],
                    'cantidad': [],
                    'sueldo_mensual': []}

        B2_Salarios_puesto = request.POST.getlist('B2_salarios_puesto')
        B2_Salarios_cantidad = request.POST.getlist('B2_salarios_cantidad')
        B2_Salarios_sueldo_mensual = request.POST.getlist('B2_salarios_sueldo_mensual')
        for B2_Salarios_puesto, B2_Salarios_cantidad, B2_Salarios_sueldo_mensual in \
                zip(B2_Salarios_puesto, B2_Salarios_cantidad, B2_Salarios_sueldo_mensual):
            salarios['puesto'].append(B2_Salarios_puesto)
            salarios['cantidad'].append(int(B2_Salarios_cantidad))
            salarios['sueldo_mensual'].append(float(B2_Salarios_sueldo_mensual))

        salarios['sueldo_diario'] = [sueldo_diario / 30 for sueldo_diario
                                     in salarios['sueldo_mensual']]
        salarios['sueldo_anual'] = [sueldo_anual * 12 for sueldo_anual
                                    in salarios['sueldo_mensual']]
        salarios['total_sueldo_mensual'] = [sum(salarios['sueldo_mensual'])]
        salarios['total_sueldo_anual'] = [sum(salarios['sueldo_anual'])]



        servicios = {'concepto': [],
                     'importe_mensual': []}

        B2_Servicios_concepto = request.POST.getlist('B2_servicios_concepto')
        B2_Servicios_importe_mensual = request.POST.getlist('B2_servicios_importe_mensual')
        for B2_Servicios_concepto, B2_Servicios_importe_mensual \
            in zip(B2_Servicios_concepto, B2_Servicios_importe_mensual):
            servicios['concepto'].append(B2_Servicios_concepto)
            servicios['importe_mensual'].append(float(B2_Servicios_importe_mensual))

        servicios['importe_2meses'] = [importe_mensual * 2 for importe_mensual in servicios['importe_mensual']]
        servicios['importe_anual'] = [importe_anual * 12 for importe_anual in servicios['importe_mensual']]
        servicios['mensual_total'] = [sum(servicios['importe_mensual'])]
        servicios['anual_total'] = [sum(servicios['importe_anual'])]



        servicios_mantto = {'concepto': [],
                            'importe_mensual': []}

        B2_Servicios_mantto_concepto = request.POST.getlist('B2_servicios_mantto_concepto')
        B2_Servicios_mantto_importe_mensual = request.POST.getlist('B2_servicios_mantto_importe_mensual')
        for B2_Servicios_mantto_concepto, B2_Servicios_mantto_importe_mensual \
            in zip(B2_Servicios_mantto_concepto, B2_Servicios_mantto_importe_mensual):
            servicios_mantto['concepto'].append(B2_Servicios_mantto_concepto)
            servicios_mantto['importe_mensual'].append(float(B2_Servicios_mantto_importe_mensual))

        servicios_mantto['importe_2meses'] = [importe_mensual * 2 for importe_mensual
                                              in servicios_mantto['importe_mensual']]
        servicios_mantto['importe_anual'] = [importe_anual * 12 for importe_anual
                                             in servicios_mantto['importe_mensual']]
        servicios_mantto['mensual_total'] = [sum(servicios_mantto['importe_mensual'])]
        servicios_mantto['anual_total'] = [sum(servicios_mantto['importe_anual'])]

        #//////////////////////////////////////////////////////////////////////////////////////////7

        capital_trabajo_mano_obra = {'unidad': [],
                                     'cantidad': [],
                                     'costo_unitario': [sum(salarios['sueldo_mensual'])]}

        B1_Capital_trabajo_mano_obra_unidad = request.POST.getlist('B1_mano_obra_unidad')
        B1_Capital_trabajo_mano_obra_cantidad = request.POST.getlist('B1_mano_obra_cantidad')

        for B1_Capital_trabajo_mano_obra_unidad, B1_Capital_trabajo_mano_obra_cantidad \
            in zip (B1_Capital_trabajo_mano_obra_unidad,B1_Capital_trabajo_mano_obra_cantidad):
            capital_trabajo_mano_obra['unidad'].append(B1_Capital_trabajo_mano_obra_unidad)
            capital_trabajo_mano_obra['cantidad'].append(int(B1_Capital_trabajo_mano_obra_cantidad))

        capital_trabajo_mano_obra['montos'] = [costo_unitario * cantidad for costo_unitario, cantidad in
                                               zip(capital_trabajo_mano_obra['costo_unitario'],
                                                   capital_trabajo_mano_obra['cantidad'])]
        capital_trabajo_mano_obra['programa'] = [montos for montos in capital_trabajo_mano_obra['montos']]
        capital_trabajo_mano_obra['socios'] = [montos for montos in capital_trabajo_mano_obra['montos']]
        capital_trabajo_mano_obra['total'] = [sum(capital_trabajo_mano_obra['programa']
                                                  + capital_trabajo_mano_obra['socios'])]

        capital_trabajo_servicios = {'unidad': [],
                                     'cantidad': [],
                                     'costo_unitario': [sum(servicios['importe_mensual'])]}

        B1_Capital_trabajo_servicios_unidad = request.POST.getlist('B1_servicios_unidad')
        B1_Capital_trabajo_servicios_cantidad = request.POST.getlist('B1_servicios_cantidad')
        for B1_Capital_trabajo_servicios_unidad, B1_Capital_trabajo_servicios_cantidad \
            in zip(B1_Capital_trabajo_servicios_unidad, B1_Capital_trabajo_servicios_cantidad):
            capital_trabajo_servicios['unidad'].append(B1_Capital_trabajo_servicios_unidad)
            capital_trabajo_servicios['cantidad'].append(int(B1_Capital_trabajo_servicios_cantidad))

        capital_trabajo_servicios['montos'] = [costo_unitario * cantidad for costo_unitario, cantidad in
                                               zip(capital_trabajo_servicios['costo_unitario'],
                                                   capital_trabajo_servicios['cantidad'])]
        capital_trabajo_servicios['programa'] = [montos for montos in capital_trabajo_servicios['montos']]
        capital_trabajo_servicios['socios'] = [montos for montos in capital_trabajo_servicios['montos']]
        capital_trabajo_servicios['total'] = [sum(capital_trabajo_servicios['programa']
                                                  + capital_trabajo_servicios['socios'])]

        capital_trabajo_servicios_mantto = {'unidad': [],
                                            'cantidad': [],
                                            'costo_unitario': [sum(servicios_mantto['importe_mensual'])]}

        B1_Capital_trabajo_servicios_mantto_unidad = request.POST.getlist('B1_servicios_mantto_unidad')
        B1_Capital_trabajo_servicios_mantto_cantidad = request.POST.getlist('B1_servicios_mantto_cantidad')
        for B1_Capital_trabajo_servicios_mantto_unidad, B1_Capital_trabajo_servicios_mantto_cantidad \
            in zip(B1_Capital_trabajo_servicios_mantto_unidad, B1_Capital_trabajo_servicios_mantto_cantidad):
            capital_trabajo_servicios_mantto['unidad'].append(B1_Capital_trabajo_servicios_mantto_unidad)
            capital_trabajo_servicios_mantto['cantidad'].append(int(B1_Capital_trabajo_servicios_mantto_cantidad))

        capital_trabajo_servicios_mantto['montos'] = [costo_unitario * cantidad for costo_unitario, cantidad
                                                      in zip(capital_trabajo_servicios_mantto['costo_unitario'],
                                                          capital_trabajo_servicios_mantto['cantidad'])]
        capital_trabajo_servicios_mantto['programa'] = [montos for montos in capital_trabajo_servicios_mantto['montos']]
        capital_trabajo_servicios_mantto['socios'] = [montos for montos in capital_trabajo_servicios_mantto['montos']]
        capital_trabajo_servicios_mantto['total'] = [sum(capital_trabajo_servicios_mantto['programa']
                                                         + capital_trabajo_servicios_mantto['socios'])]

        total_presupuesto_inversion = {'total_monto': [sum(capital_trabajo_servicios['montos']
                                                          + capital_trabajo_mano_obra['montos'] +
                                                          capital_trabajo_servicios_mantto['montos']
                                                          + activo_fijo['montos'] + Activo_diferido['montos'])],

                                       'total_programa': [sum(capital_trabajo_servicios['programa']
                                                             + capital_trabajo_mano_obra['programa'] +
                                                             capital_trabajo_servicios_mantto['programa']
                                                             + activo_fijo['programa'] + Activo_diferido['programa'])],

                                       'total_socios': [sum(capital_trabajo_servicios['socios']
                                                           + capital_trabajo_mano_obra['socios'] +
                                                           capital_trabajo_servicios_mantto['socios']
                                                           + activo_fijo['socios'] + Activo_diferido['socios'])],
                                       }
        total_presupuesto_inversion['total_B1'] = [sum(total_presupuesto_inversion['total_programa']
                                                       + total_presupuesto_inversion['total_socios'])]

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # BLOQUE 2: MEMORIAS DE CALCULO
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        costo_materiales = {'materiales': [],
                            'unidad': [],
                            'costo_unitario': []}

        B2_Costo_materiales_materiales = request.POST.getlist('B2_costo_materiales_materiales')
        B2_Costo_materiales_unidad = request.POST.getlist('B2_costo_materiales_unidad')
        B2_Costo_materiales_costo_unitario = request.POST.getlist('B2_costo_materiales_costo_unitario')
        for B2_Costo_materiales_materiales, B2_Costo_materiales_unidad, B2_Costo_materiales_costo_unitario \
            in zip(B2_Costo_materiales_materiales, B2_Costo_materiales_unidad, B2_Costo_materiales_costo_unitario):
            costo_materiales['materiales'].append(B2_Costo_materiales_materiales)
            costo_materiales['unidad'].append(B2_Costo_materiales_unidad)
            costo_materiales['costo_unitario'].append(float(B2_Costo_materiales_costo_unitario))

        registro_propiedad_intelectual = {'concepto': [],
                                          'cantidad': [],
                                          'precio_unitario': []}

        B2_Registro_propiedad_intelectual_concepto = request.POST.getlist('B2_registro_propiedad_intelectual_concepto')
        B2_Registro_propiedad_intelectual_cantidad = request.POST.getlist('B2_registro_propiedad_intelectual_cantidad')
        B2_Registro_propiedad_intelectual_precio_unitario = request.POST.getlist('B2_registro_propiedad_intelectual_precio_unitario')
        for B2_Registro_propiedad_intelectual_concepto, B2_Registro_propiedad_intelectual_cantidad, B2_Registro_propiedad_intelectual_precio_unitario \
            in zip(B2_Registro_propiedad_intelectual_concepto, B2_Registro_propiedad_intelectual_cantidad, B2_Registro_propiedad_intelectual_precio_unitario):
            registro_propiedad_intelectual['concepto'].append(B2_Registro_propiedad_intelectual_concepto)
            registro_propiedad_intelectual['cantidad'].append(int(B2_Registro_propiedad_intelectual_cantidad))
            registro_propiedad_intelectual['precio_unitario'].append(float(B2_Registro_propiedad_intelectual_precio_unitario))

        registro_propiedad_intelectual['precio_total'] = [cantidad * precio_unitario for cantidad, precio_unitario
                                                          in zip(registro_propiedad_intelectual['cantidad'],
                                                                 registro_propiedad_intelectual['precio_unitario'])]
        registro_propiedad_intelectual['total'] = [sum(registro_propiedad_intelectual['precio_total'])]

        servicios_administrativos = {'concepto': [],
                                     'cantidad': [],
                                     'precio_unitario': []}

        B2_Servicios_administrativos_concepto = request.POST.getlist('B2_servicios_administrativos_concepto')
        B2_Servicios_administrativos_cantidad = request.POST.getlist('B2_servicios_administrativos_cantidad')
        B2_Servicios_administrativos_precio_unitario = request.POST.getlist('B2_servicios_administrativos_precio_unitario')
        for B2_Servicios_administrativos_concepto, B2_Servicios_administrativos_cantidad, B2_Servicios_administrativos_precio_unitario \
            in zip(B2_Servicios_administrativos_concepto, B2_Servicios_administrativos_cantidad, B2_Servicios_administrativos_precio_unitario):
            servicios_administrativos['concepto'].append(B2_Servicios_administrativos_concepto)
            servicios_administrativos['cantidad'].append(int(B2_Servicios_administrativos_cantidad))
            servicios_administrativos['precio_unitario'].append(float(B2_Servicios_administrativos_precio_unitario))

        servicios_administrativos['precio_total'] = [cantidad * precio_unitario for cantidad, precio_unitario
                                                     in zip(servicios_administrativos['cantidad'],
                                                            servicios_administrativos['precio_unitario'])]
        servicios_administrativos['total'] = [sum(servicios_administrativos['precio_total'])]



        costo_proyecto1_mensual = {'costo_mensual': [sum(servicios['importe_mensual'] + salarios['sueldo_mensual']+ servicios_administrativos['precio_unitario'] + servicios_mantto['mensual_total'])]}
        costo_proyecto1_mensual['costo_dia'] = [costo_dia / 30 for costo_dia in costo_proyecto1_mensual['costo_mensual']]


        costo_materiales['por_dia'] = [costo_dia / 30 for costo_dia in costo_proyecto1_mensual['costo_mensual']]


        memorias_calculo = {'concepto': [],
                            'presentacion': [],
                            'ventas_semana': [],
                            'costo_insumo': []}

        B2_Memorias_calculo_costo_insumo = request.POST.getlist('B2_memorias_calculo_costo_insumo')
        B2_Memorias_calculo_concepto = request.POST.getlist('B2_memorias_calculo_concepto')
        B2_Memorias_calculo_presentacion = request.POST.getlist('B2_memorias_calculo_presentacion')
        B2_Memorias_calculo_ventas_semana = request.POST.getlist('B2_memorias_calculo_ventas_semana')
        for B2_Memorias_calculo_concepto, B2_Memorias_calculo_presentacion, B2_Memorias_calculo_ventas_semana, B2_Memorias_calculo_costo_insumo \
            in zip(B2_Memorias_calculo_concepto, B2_Memorias_calculo_presentacion, B2_Memorias_calculo_ventas_semana, B2_Memorias_calculo_costo_insumo):
            memorias_calculo['concepto'].append(B2_Memorias_calculo_concepto)
            memorias_calculo['presentacion'].append(B2_Memorias_calculo_presentacion)
            memorias_calculo['ventas_semana'].append(int(B2_Memorias_calculo_ventas_semana))
            memorias_calculo['costo_insumo'].append(float(B2_Memorias_calculo_costo_insumo))

        memorias_calculo['costo_semanal'] = [costo_insumo * ventas_semana for costo_insumo, ventas_semana
                                             in zip(memorias_calculo['costo_insumo'], memorias_calculo['ventas_semana'])]
        memorias_calculo['costo_mensual'] = [costo_semanal * 4 for costo_semanal in memorias_calculo['costo_semanal']]
        memorias_calculo['precio_venta'] = [costo_insumo * 1.35 for costo_insumo in memorias_calculo['costo_insumo']]
        memorias_calculo['ingreso_semanal'] = [precio_venta * ventas_semana for precio_venta, ventas_semana in
                                               zip(memorias_calculo['precio_venta'], memorias_calculo['ventas_semana'])]
        memorias_calculo['ingreso_mensual'] = [ingreso_semanal * 4 for ingreso_semanal in
                                               memorias_calculo['ingreso_semanal']]
        memorias_calculo['ingreso_anual'] = [ingreso_mensual * 12 for ingreso_mensual in
                                             memorias_calculo['ingreso_mensual']]
        memorias_calculo['total_ventas_semana'] = [sum(memorias_calculo['ventas_semana'])]
        memorias_calculo['total_costo_semana'] = [sum(memorias_calculo['costo_semanal'])]
        memorias_calculo['total_costo_mensual'] = [sum(memorias_calculo['costo_mensual'])]
        memorias_calculo['total_ingreso_semanal'] = [sum(memorias_calculo['ingreso_semanal'])]
        memorias_calculo['total_ingreso_mensual'] = [sum(memorias_calculo['ingreso_mensual'])]
        memorias_calculo['total_ingreso_anual'] = [sum(memorias_calculo['ingreso_anual'])]
        memorias_calculo['ganacia_semanal'] = [total_ingreso_semanal - total_costo_semana
                                               for total_ingreso_semanal, total_costo_semana
                                               in zip(memorias_calculo['total_ingreso_semanal'],
                                                      memorias_calculo['total_costo_semana'])]
        memorias_calculo['ganancia_mensual'] = [ganancia_semanal * 4 for ganancia_semanal in
                                                memorias_calculo['ganacia_semanal']]
        memorias_calculo['ganancia_anual'] = [ganancia_mensual * 12 for ganancia_mensual in
                                              memorias_calculo['ganancia_mensual']]

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # BLOQUE 3: PROYECCION DE COSTOS
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        costos_proyecto1 = {'concepto': servicios['concepto'] + servicios_mantto['concepto']
                                        + servicios_administrativos['concepto'] + salarios['puesto'],
                            'costo_mensual': servicios['importe_mensual'] + servicios_mantto['importe_mensual'] +
                                              servicios_administrativos['precio_unitario'] + salarios['sueldo_mensual']}

        costos_proyecto1['ano1'] = [costo_mensual * 12 for costo_mensual in costos_proyecto1['costo_mensual']]
        costos_proyecto1['ano2'] = [ano1 * 1.02 for ano1 in costos_proyecto1['ano1']]
        costos_proyecto1['ano3'] = [ano2 * 1.02 for ano2 in costos_proyecto1['ano2']]
        costos_proyecto1['ano4'] = [ano3 * 1.02 for ano3 in costos_proyecto1['ano3']]
        costos_proyecto1['ano5'] = [ano4 * 1.02 for ano4 in costos_proyecto1['ano4']]

        costos_proyecto2 = {'concepto': [concepto for concepto in memorias_calculo['concepto']],
                            'costo_mensual': [costo_mensual for costo_mensual in memorias_calculo['costo_mensual']]}
        costos_proyecto2['ano1'] = [costo_mensual * 12 for costo_mensual in costos_proyecto2['costo_mensual']]
        costos_proyecto2['ano2'] = [ano1 * 1.02 for ano1 in costos_proyecto2['ano1']]
        costos_proyecto2['ano3'] = [ano2 * 1.02 for ano2 in costos_proyecto2['ano2']]
        costos_proyecto2['ano4'] = [ano3 * 1.02 for ano3 in costos_proyecto2['ano3']]
        costos_proyecto2['ano5'] = [ano4 * 1.02 for ano4 in costos_proyecto2['ano4']]

        totales = {'total_costo_mensual': [sum(costos_proyecto1['costo_mensual'] + costos_proyecto2['costo_mensual'])],
                   'total_ano1': [sum(costos_proyecto1['ano1'] + costos_proyecto2['ano1'])],
                   'total_ano2': [sum(costos_proyecto1['ano2'] + costos_proyecto2['ano2'])],
                   'total_ano3': [sum(costos_proyecto1['ano3'] + costos_proyecto2['ano3'])],
                   'total_ano4': [sum(costos_proyecto1['ano4'] + costos_proyecto2['ano4'])],
                   'total_ano5': [sum(costos_proyecto1['ano5'] + costos_proyecto2['ano5'])]}


        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # BLOQUE 4: COSTOS TOTALES
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        costos_fijos = {'concepto': servicios['concepto'] + servicios_administrativos['concepto']
                                    + servicios_mantto['concepto'] + salarios['puesto'],
                        'ano1': [ano1 for ano1 in costos_proyecto1['ano1']],
                        'ano2': [ano2 for ano2 in costos_proyecto1['ano2']],
                        'ano3': [ano3 for ano3 in costos_proyecto1['ano3']],
                        'ano4': [ano4 for ano4 in costos_proyecto1['ano4']],
                        'ano5': [ano5 for ano5 in costos_proyecto1['ano5']]}
        costos_fijos['total_ano1'] = [sum(costos_fijos['ano1'])]
        costos_fijos['total_ano2'] = [sum(costos_fijos['ano2'])]
        costos_fijos['total_ano3'] = [sum(costos_fijos['ano3'])]
        costos_fijos['total_ano4'] = [sum(costos_fijos['ano4'])]
        costos_fijos['total_ano5'] = [sum(costos_fijos['ano5'])]



        costos_variables = {'concepto': [concepto for concepto in costos_proyecto2['concepto']],
                            'ano1': [ano1 for ano1 in costos_proyecto2['ano1']],
                            'ano2': [ano2 for ano2 in costos_proyecto2['ano2']],
                            'ano3': [ano3 for ano3 in costos_proyecto2['ano3']],
                            'ano4': [ano4 for ano4 in costos_proyecto2['ano4']],
                            'ano5': [ano5 for ano5 in costos_proyecto2['ano5']]}
        costos_variables['total_ano1'] = [sum(costos_variables['ano1'])]
        costos_variables['total_ano2'] = [sum(costos_variables['ano2'])]
        costos_variables['total_ano3'] = [sum(costos_variables['ano3'])]
        costos_variables['total_ano4'] = [sum(costos_variables['ano4'])]
        costos_variables['total_ano5'] = [sum(costos_variables['ano5'])]



        costos_totales = {'costo_fijo_ano1': [total_ano1 for total_ano1 in costos_fijos['total_ano1']],
                          'costo_fijo_ano2': [total_ano2 for total_ano2 in costos_fijos['total_ano2']],
                          'costo_fijo_ano3': [total_ano3 for total_ano3 in costos_fijos['total_ano3']],
                          'costo_fijo_ano4': [total_ano4 for total_ano4 in costos_fijos['total_ano4']],
                          'costo_fijo_ano5': [total_ano5 for total_ano5 in costos_fijos['total_ano5']],
                          'costo_variable_ano1': [total_ano1 for total_ano1 in costos_variables['total_ano1']],
                          'costo_variable_ano2': [total_ano2 for total_ano2 in costos_variables['total_ano2']],
                          'costo_variable_ano3': [total_ano3 for total_ano3 in costos_variables['total_ano3']],
                          'costo_variable_ano4': [total_ano4 for total_ano4 in costos_variables['total_ano4']],
                          'costo_variable_ano5': [total_ano5 for total_ano5 in costos_variables['total_ano5']]}



        costos_totales['costos_totales_ano1'] = [
            sum(costos_totales['costo_fijo_ano1'] + costos_totales['costo_variable_ano1'])]
        costos_totales['costos_totales_ano2'] = [
            sum(costos_totales['costo_fijo_ano2'] + costos_totales['costo_variable_ano2'])]
        costos_totales['costos_totales_ano3'] = [
            sum(costos_totales['costo_fijo_ano3'] + costos_totales['costo_variable_ano3'])]
        costos_totales['costos_totales_ano4'] = [
            sum(costos_totales['costo_fijo_ano4'] + costos_totales['costo_variable_ano4'])]
        costos_totales['costos_totales_ano5'] = [
            sum(costos_totales['costo_fijo_ano5'] + costos_totales['costo_variable_ano5'])]

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
        proyeccion_ingresos['ano1'] = [ventas_mensual * 12 for ventas_mensual
                                       in proyeccion_ingresos['ventas_mensual']]
        proyeccion_ingresos['ano2'] = [ano1 * 1.05 for ano1
                                       in proyeccion_ingresos['ano1']]
        proyeccion_ingresos['ano3'] = [ano2 * 1.05 for ano2
                                       in proyeccion_ingresos['ano2']]
        proyeccion_ingresos['ano4'] = [ano3 * 1.05 for ano3
                                       in proyeccion_ingresos['ano3']]
        proyeccion_ingresos['ano5'] = [ano4 * 1.05 for ano4
                                       in proyeccion_ingresos['ano4']]
        proyeccion_ingresos['total_ventas_mensual'] = [sum(proyeccion_ingresos['ventas_mensual'])]
        proyeccion_ingresos['total_ano1'] = [sum(proyeccion_ingresos['ano1'])]
        proyeccion_ingresos['total_ano2'] = [sum(proyeccion_ingresos['ano2'])]
        proyeccion_ingresos['total_ano3'] = [sum(proyeccion_ingresos['ano3'])]
        proyeccion_ingresos['total_ano4'] = [sum(proyeccion_ingresos['ano4'])]
        proyeccion_ingresos['total_ano5'] = [sum(proyeccion_ingresos['ano5'])]

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # BLOQUE 6: ESTADO DE RESULTADOS
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        costos_depreciaciones = {'activo_fijo': [concepto for concepto in
                                                 activo_fijo['concepto']],
                                 'valor_original': [montos for montos in
                                                    activo_fijo['montos']],
                                 'tasa': 0.10,
                                 'anos': 5}
        costos_depreciaciones['depreciacion_anual'] = [valor_original * 0.10
                                                       for valor_original
                                                       in costos_depreciaciones['valor_original']]
        costos_depreciaciones['valor_rescate'] = [valor_original - (depreciacion_anual * costos_depreciaciones['anos'])
                                                  for valor_original, depreciacion_anual
                                                  in zip(costos_depreciaciones['valor_original'],
                                                         costos_depreciaciones['depreciacion_anual'])]
        costos_depreciaciones['total_valor_original'] = [sum(costos_depreciaciones['valor_original'])]
        costos_depreciaciones['total_depreciacion_anual'] = [sum(costos_depreciaciones['depreciacion_anual'])]
        costos_depreciaciones['total_valor_rescate'] = sum(costos_depreciaciones['valor_rescate'])



        estado_resultados = {'ventas_ano1': [total_ventas_ano1 for total_ventas_ano1
                                             in proyeccion_ingresos['total_ano1']],
                             'ventas_ano2': [total_ventas_ano2 for total_ventas_ano2
                                             in proyeccion_ingresos['total_ano2']],
                             'ventas_ano3': [total_ventas_ano3 for total_ventas_ano3
                                             in proyeccion_ingresos['total_ano3']],
                             'ventas_ano4': [total_ventas_ano4 for total_ventas_ano4
                                             in proyeccion_ingresos['total_ano4']],
                             'ventas_ano5': [total_ventas_ano5 for total_ventas_ano5
                                             in proyeccion_ingresos['total_ano5']],
                             'costos_fijos_ano1': [total_costos_ano1 for total_costos_ano1
                                                   in costos_fijos['total_ano1']],
                             'costos_fijos_ano2': [total_costos_ano2 for total_costos_ano2
                                                   in costos_fijos['total_ano2']],
                             'costos_fijos_ano3': [total_costos_ano3 for total_costos_ano3
                                                   in costos_fijos['total_ano3']],
                             'costos_fijos_ano4': [total_costos_ano4 for total_costos_ano4
                                                   in costos_fijos['total_ano4']],
                             'costos_fijos_ano5': [total_costos_ano5 for total_costos_ano5
                                                   in costos_fijos['total_ano5']],
                             'costos_variables_ano1': [costos_variables_ano1 for costos_variables_ano1
                                                       in costos_variables['total_ano1']],
                             'costos_variables_ano2': [costos_variables_ano2 for costos_variables_ano2
                                                       in costos_variables['total_ano2']],
                             'costos_variables_ano3': [costos_variables_ano3 for costos_variables_ano3
                                                       in costos_variables['total_ano3']],
                             'costos_variables_ano4': [costos_variables_ano4 for costos_variables_ano4
                                                       in costos_variables['total_ano4']],
                             'costos_variables_ano5': [costos_variables_ano5 for costos_variables_ano5
                                                       in costos_variables['total_ano5']]}
        estado_resultados['costos_totales_ano1'] = [costos_fijos_ano1 + costos_variables_ano1
                                                    for costos_fijos_ano1, costos_variables_ano1
                                                    in zip(estado_resultados['costos_fijos_ano1'],
                                                           estado_resultados['costos_variables_ano1'])]
        estado_resultados['costos_totales_ano2'] = [costos_fijos_ano2 + costos_variables_ano2
                                                    for costos_fijos_ano2, costos_variables_ano2
                                                    in zip(estado_resultados['costos_fijos_ano2'],
                                                           estado_resultados['costos_variables_ano2'])]
        estado_resultados['costos_totales_ano3'] = [costos_fijos_ano3 + costos_variables_ano3
                                                    for costos_fijos_ano3, costos_variables_ano3
                                                    in zip(estado_resultados['costos_fijos_ano3'],
                                                           estado_resultados['costos_variables_ano3'])]
        estado_resultados['costos_totales_ano4'] = [costos_fijos_ano4 + costos_varibales_ano4
                                                    for costos_fijos_ano4, costos_varibales_ano4
                                                    in zip(estado_resultados['costos_fijos_ano4'],
                                                           estado_resultados['costos_variables_ano4'])]
        estado_resultados['costos_totales_ano5'] = [costos_fijos_ano5 + costos_variables_ano5
                                                    for costos_fijos_ano5, costos_variables_ano5
                                                    in zip(estado_resultados['costos_fijos_ano5'],
                                                           estado_resultados['costos_variables_ano5'])]
        estado_resultados['utilidad_bruta_ano1'] = [ventas_ano1 - costos_totales_ano1
                                                    for ventas_ano1, costos_totales_ano1
                                                    in zip(estado_resultados['ventas_ano1'],
                                                           estado_resultados['costos_totales_ano1'])]
        estado_resultados['utilidad_bruta_ano2'] = [ventas_ano2 - costos_totales_ano2
                                                    for ventas_ano2, costos_totales_ano2
                                                    in zip(estado_resultados['ventas_ano2'],
                                                           estado_resultados['costos_totales_ano2'])]
        estado_resultados['utilidad_bruta_ano3'] = [ventas_ano3 - costos_totales_ano3
                                                    for ventas_ano3, costos_totales_ano3
                                                    in zip(estado_resultados['ventas_ano3'],
                                                           estado_resultados['costos_totales_ano3'])]
        estado_resultados['utilidad_bruta_ano4'] = [ventas_ano4 - costos_totales_ano4
                                                    for ventas_ano4, costos_totales_ano4
                                                    in zip(estado_resultados['ventas_ano4'],
                                                           estado_resultados['costos_totales_ano4'])]
        estado_resultados['utilidad_bruta_ano5'] = [ventas_ano5 - costos_totales_ano5
                                                    for ventas_ano5, costos_totales_ano5
                                                    in zip(estado_resultados['ventas_ano5'],
                                                           estado_resultados['costos_totales_ano5'])]
        estado_resultados['depreciacion_ano1'] = [total_depreciacion_anual for total_depreciacion_anual
                                                  in costos_depreciaciones['total_depreciacion_anual']]
        estado_resultados['depreciacion_ano2'] = [depreciacion_ano1 * 1.05 for depreciacion_ano1
                                                  in estado_resultados['depreciacion_ano1']]
        estado_resultados['depreciacion_ano3'] = [depreciacion_ano2 * 1.05 for depreciacion_ano2
                                                  in estado_resultados['depreciacion_ano2']]
        estado_resultados['depreciacion_ano4'] = [depreciacion_ano3 * 1.05 for depreciacion_ano3
                                                  in estado_resultados['depreciacion_ano3']]
        estado_resultados['depreciacion_ano5'] = [depreciacion_ano4 * 1.05 for depreciacion_ano4
                                                  in estado_resultados['depreciacion_ano4']]
        estado_resultados['utilidad_antes_impuestos_ano1'] = [utilidad_bruta_ano1 - depreciacion_ano1
                                                              for utilidad_bruta_ano1, depreciacion_ano1
                                                              in zip(estado_resultados['utilidad_bruta_ano1'],
                                                                     estado_resultados['depreciacion_ano1'])]
        estado_resultados['utilidad_antes_impuestos_ano2'] = [utilidad_bruta_ano2 - depreciacion_ano2
                                                              for utilidad_bruta_ano2, depreciacion_ano2
                                                              in zip(estado_resultados['utilidad_bruta_ano2'],
                                                                     estado_resultados['depreciacion_ano2'])]
        estado_resultados['utilidad_antes_impuestos_ano3'] = [utilidad_bruta_ano3 - depreciacion_ano3
                                                              for utilidad_bruta_ano3, depreciacion_ano3
                                                              in zip(estado_resultados['utilidad_bruta_ano3'],
                                                                     estado_resultados['depreciacion_ano3'])]
        estado_resultados['utilidad_antes_impuestos_ano4'] = [utilidad_bruta_ano4 - depreciacion_ano4
                                                              for utilidad_bruta_ano4, depreciacion_ano4
                                                              in zip(estado_resultados['utilidad_bruta_ano4'],
                                                                     estado_resultados['depreciacion_ano4'])]
        estado_resultados['utilidad_antes_impuestos_ano5'] = [utilidad_bruta_ano5 - depreciacion_ano5
                                                              for utilidad_bruta_ano5, depreciacion_ano5
                                                              in zip(estado_resultados['utilidad_bruta_ano5'],
                                                                     estado_resultados['depreciacion_ano5'])]
        estado_resultados['impuestos_ano1'] = [utilidad_antes_impuestos_ano1 * costos_depreciaciones['tasa']
                                               for utilidad_antes_impuestos_ano1
                                               in estado_resultados['utilidad_antes_impuestos_ano1']]
        estado_resultados['impuestos_ano2'] = [utilidad_antes_impuestos_ano2 * costos_depreciaciones['tasa']
                                               for utilidad_antes_impuestos_ano2
                                               in estado_resultados['utilidad_antes_impuestos_ano2']]
        estado_resultados['impuestos_ano3'] = [utilidad_antes_impuestos_ano3 * costos_depreciaciones['tasa']
                                               for utilidad_antes_impuestos_ano3
                                               in estado_resultados['utilidad_antes_impuestos_ano3']]
        estado_resultados['impuestos_ano4'] = [utilidad_antes_impuestos_ano4 * costos_depreciaciones['tasa']
                                               for utilidad_antes_impuestos_ano4
                                               in estado_resultados['utilidad_antes_impuestos_ano4']]
        estado_resultados['impuestos_ano5'] = [utilidad_antes_impuestos_ano5 * costos_depreciaciones['tasa']
                                               for utilidad_antes_impuestos_ano5
                                               in estado_resultados['utilidad_antes_impuestos_ano5']]
        estado_resultados['utilidad_ejercicio_ano1'] = [utilidad_antes_impuestos_ano1 - impuestos_ano1
                                                        for utilidad_antes_impuestos_ano1, impuestos_ano1
                                                        in zip(estado_resultados['utilidad_antes_impuestos_ano1'],
                                                               estado_resultados['impuestos_ano1'])]
        estado_resultados['utilidad_ejercicio_ano2'] = [utilidad_antes_impuestos_ano2 - impuestos_ano2
                                                        for utilidad_antes_impuestos_ano2, impuestos_ano2
                                                        in zip(estado_resultados['utilidad_antes_impuestos_ano2'],
                                                               estado_resultados['impuestos_ano2'])]
        estado_resultados['utilidad_ejercicio_ano3'] = [utilidad_antes_impuestos_ano3 - impuestos_ano3
                                                        for utilidad_antes_impuestos_ano3, impuestos_ano3
                                                        in zip(estado_resultados['utilidad_antes_impuestos_ano3'],
                                                               estado_resultados['impuestos_ano3'])]
        estado_resultados['utilidad_ejercicio_ano4'] = [utilidad_antes_impuestos_ano4 - impuestos_ano4
                                                        for utilidad_antes_impuestos_ano4, impuestos_ano4
                                                        in zip(estado_resultados['utilidad_antes_impuestos_ano4'],
                                                               estado_resultados['impuestos_ano4'])]
        estado_resultados['utilidad_ejercicio_ano5'] = [utilidad_antes_impuestos_ano5 - impuestos_ano5
                                                        for utilidad_antes_impuestos_ano5, impuestos_ano5
                                                        in zip(estado_resultados['utilidad_antes_impuestos_ano5'],
                                                               estado_resultados['impuestos_ano5'])]

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # BLOQUE 7: FLUJO DE EFECTIVO
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        flujo_efectivo = {'ventas_ano1': [total_ano1 for total_ano1
                                          in proyeccion_ingresos['total_ano1']],
                          'ventas_ano2': [total_ano2 for total_ano2
                                          in proyeccion_ingresos['total_ano2']],
                          'ventas_ano3': [total_ano3 for total_ano3
                                          in proyeccion_ingresos['total_ano3']],
                          'ventas_ano4': [total_ano4 for total_ano4
                                          in proyeccion_ingresos['total_ano4']],
                          'ventas_ano5': [total_ano5 for total_ano5
                                          in proyeccion_ingresos['total_ano5']],
                          'valor_rescate': [costos_depreciaciones['total_valor_rescate']]}
        flujo_efectivo['ingresos_totales_ano1'] = [ventas_ano1 for ventas_ano1
                                                   in flujo_efectivo['ventas_ano1']]
        flujo_efectivo['ingresos_totales_ano2'] = [ventas_ano2 for ventas_ano2
                                                   in flujo_efectivo['ventas_ano2']]
        flujo_efectivo['ingresos_totales_ano3'] = [ventas_ano3 for ventas_ano3
                                                   in flujo_efectivo['ventas_ano3']]
        flujo_efectivo['ingresos_totales_ano4'] = [ventas_ano4 for ventas_ano4
                                                   in flujo_efectivo['ventas_ano4']]
        flujo_efectivo['ingresos_totales_ano5'] = [ventas_ano5 + valor_rescate
                                                   for ventas_ano5, valor_rescate
                                                   in zip(flujo_efectivo['ventas_ano5'],
                                                          flujo_efectivo['valor_rescate'])]
        flujo_efectivo['costos_fijos_ano1'] = [total_ano1 for total_ano1
                                               in costos_fijos['total_ano1']]
        flujo_efectivo['costos_fijos_ano2'] = [total_ano2 for total_ano2
                                               in costos_fijos['total_ano2']]
        flujo_efectivo['costos_fijos_ano3'] = [total_ano3 for total_ano3
                                               in costos_fijos['total_ano3']]
        flujo_efectivo['costos_fijos_ano4'] = [total_ano4 for total_ano4
                                               in costos_fijos['total_ano4']]
        flujo_efectivo['costos_fijos_ano5'] = [total_ano5 for total_ano5
                                               in costos_fijos['total_ano5']]
        flujo_efectivo['costos_variables_ano1'] = [total_ano1 for total_ano1
                                                   in costos_variables['total_ano1']]
        flujo_efectivo['costos_variables_ano2'] = [total_ano2 for total_ano2
                                                   in costos_variables['total_ano2']]
        flujo_efectivo['costos_variables_ano3'] = [total_ano3 for total_ano3
                                                   in costos_variables['total_ano3']]
        flujo_efectivo['costos_variables_ano4'] = [total_ano4 for total_ano4
                                                   in costos_variables['total_ano4']]
        flujo_efectivo['costos_variables_ano5'] = [total_ano5 for total_ano5
                                                   in costos_variables['total_ano5']]
        flujo_efectivo['costos_totales_ano1'] = [costos_fijos_ano1 + costos_variables_ano1
                                                 for costos_fijos_ano1, costos_variables_ano1
                                                 in zip(flujo_efectivo['costos_fijos_ano1'],
                                                        flujo_efectivo['costos_variables_ano1'])]
        flujo_efectivo['costos_totales_ano2'] = [costos_fijos_ano2 + costos_variables_ano2
                                                 for costos_fijos_ano2, costos_variables_ano2
                                                 in zip(flujo_efectivo['costos_fijos_ano2'],
                                                        flujo_efectivo['costos_variables_ano2'])]
        flujo_efectivo['costos_totales_ano3'] = [costos_fijos_ano3 + costos_variables_ano3
                                                 for costos_fijos_ano3, costos_variables_ano3
                                                 in zip(flujo_efectivo['costos_fijos_ano3'],
                                                        flujo_efectivo['costos_variables_ano3'])]
        flujo_efectivo['costos_totales_ano4'] = [costos_fijos_ano4 + costos_variables_ano4
                                                 for costos_fijos_ano4, costos_variables_ano4
                                                 in zip(flujo_efectivo['costos_fijos_ano4'],
                                                        flujo_efectivo['costos_variables_ano4'])]
        flujo_efectivo['costos_totales_ano5'] = [costos_fijos_ano5 + costos_variables_ano5
                                                 for costos_fijos_ano5, costos_variables_ano5
                                                 in zip(flujo_efectivo['costos_fijos_ano5'],
                                                        flujo_efectivo['costos_variables_ano5'])]
        flujo_efectivo['compra_activo_fijo'] = [sum(activo_fijo['montos'])]
        flujo_efectivo['compra_activo_diferido'] = [sum(Activo_diferido['montos'])]
        flujo_efectivo['compra_capital_trabajo'] = [sum(capital_trabajo_servicios['montos']
                                                        + capital_trabajo_servicios_mantto['montos']
                                                        + capital_trabajo_mano_obra['montos'])]
        flujo_efectivo['saldo_final_ano0'] = [compra_activo_fijo - compra_activo_diferido - compra_capital_trabajo
                                              for compra_activo_fijo, compra_activo_diferido, compra_capital_trabajo
                                              in zip(flujo_efectivo['compra_activo_fijo'],
                                                     flujo_efectivo['compra_activo_diferido'],
                                                     flujo_efectivo['compra_capital_trabajo'])]
        flujo_efectivo['saldo_final_ano1'] = [ingresos_totales_ano1 - costos_totales_ano1
                                              for ingresos_totales_ano1, costos_totales_ano1
                                              in zip(flujo_efectivo['ingresos_totales_ano1'],
                                                     flujo_efectivo['costos_totales_ano1'])]
        flujo_efectivo['saldo_final_ano2'] = [ingresos_totales_ano2 - costos_totales_ano2
                                              for ingresos_totales_ano2, costos_totales_ano2
                                              in zip(flujo_efectivo['ingresos_totales_ano2'],
                                                     flujo_efectivo['costos_totales_ano2'])]
        flujo_efectivo['saldo_final_ano3'] = [ingresos_totales_ano3 - costos_totales_ano3
                                              for ingresos_totales_ano3, costos_totales_ano3
                                              in zip(flujo_efectivo['ingresos_totales_ano3'],
                                                     flujo_efectivo['costos_totales_ano3'])]
        flujo_efectivo['saldo_final_ano4'] = [ingresos_totales_ano4 - costos_totales_ano4
                                              for ingresos_totales_ano4, costos_totales_ano4
                                              in zip(flujo_efectivo['ingresos_totales_ano4'],
                                                     flujo_efectivo['costos_totales_ano4'])]
        flujo_efectivo['saldo_final_ano5'] = [ingresos_totales_ano5 - costos_totales_ano5
                                              for ingresos_totales_ano5, costos_totales_ano5
                                              in zip(flujo_efectivo['ingresos_totales_ano5'],
                                                     flujo_efectivo['costos_totales_ano5'])]

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # BLOQUE8 : PUNTO DE EQUILIBRIO
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        punto_equilibrio = {'ventas_ano1': [total_ano1 for total_ano1
                                            in proyeccion_ingresos['total_ano1']],
                            'ventas_ano2': [total_ano2 for total_ano2
                                            in proyeccion_ingresos['total_ano2']],
                            'ventas_ano3': [total_ano3 for total_ano3
                                            in proyeccion_ingresos['total_ano3']],
                            'ventas_ano4': [total_ano4 for total_ano4
                                            in proyeccion_ingresos['total_ano4']],
                            'ventas_ano5': [total_ano5 for total_ano5
                                            in proyeccion_ingresos['total_ano5']],
                            'costos_fijos_ano1': [total_ano1 for total_ano1
                                                  in costos_fijos['total_ano1']],
                            'costos_fijos_ano2': [total_ano2 for total_ano2
                                                  in costos_fijos['total_ano2']],
                            'costos_fijos_ano3': [total_ano3 for total_ano3
                                                  in costos_fijos['total_ano3']],
                            'costos_fijos_ano4': [total_ano4 for total_ano4
                                                  in costos_fijos['total_ano4']],
                            'costos_fijos_ano5': [total_ano5 for total_ano5
                                                  in costos_fijos['total_ano5']],
                            'costos_variables_ano1': [variables_ano1 for variables_ano1
                                                      in costos_variables['total_ano1']],
                            'costos_variables_ano2': [variables_ano2 for variables_ano2
                                                      in costos_variables['total_ano2']],
                            'costos_variables_ano3': [variables_ano3 for variables_ano3
                                                      in costos_variables['total_ano3']],
                            'costos_variables_ano4': [variables_ano4 for variables_ano4
                                                      in costos_variables['total_ano4']],
                            'costos_variables_ano5': [variables_ano5 for variables_ano5
                                                      in costos_variables['total_ano5']]}
        punto_equilibrio['costos_totales_ano1'] = [costos_fijos_ano1 + costos_variables_ano1
                                                   for costos_fijos_ano1, costos_variables_ano1
                                                   in zip(punto_equilibrio['costos_fijos_ano1'],
                                                          punto_equilibrio['costos_variables_ano1'])]
        punto_equilibrio['costos_totales_ano2'] = [costos_fijos_ano2 + costos_variables_ano2
                                                   for costos_fijos_ano2, costos_variables_ano2
                                                   in zip(punto_equilibrio['costos_fijos_ano2'],
                                                          punto_equilibrio['costos_variables_ano2'])]
        punto_equilibrio['costos_totales_ano3'] = [costos_fijos_ano3 + costos_variables_ano3
                                                   for costos_fijos_ano3, costos_variables_ano3
                                                   in zip(punto_equilibrio['costos_fijos_ano3'],
                                                          punto_equilibrio['costos_variables_ano3'])]
        punto_equilibrio['costos_totales_ano4'] = [costos_fijos_ano4 + costos_variables_ano4
                                                   for costos_fijos_ano4, costos_variables_ano4
                                                   in zip(punto_equilibrio['costos_fijos_ano4'],
                                                          punto_equilibrio['costos_variables_ano4'])]
        punto_equilibrio['costos_totales_ano5'] = [costos_fijos_ano5 + costos_variables_ano5
                                                   for costos_fijos_ano5, costos_variables_ano5
                                                   in zip(punto_equilibrio['costos_fijos_ano5'],
                                                          punto_equilibrio['costos_variables_ano5'])]
        punto_equilibrio['punto_equilibrio_ano1'] = [costos_fijos_ano1 / (1 - costos_variables_ano1 / ventas_ano1)
                                                     for costos_fijos_ano1, costos_variables_ano1, ventas_ano1
                                                     in zip(punto_equilibrio['costos_fijos_ano1'],
                                                            punto_equilibrio['costos_variables_ano1'],
                                                            punto_equilibrio['ventas_ano1'])]
        punto_equilibrio['punto_equilibrio_ano2'] = [costos_fijos_ano2 / (1 - costos_variables_ano2 / ventas_ano2)
                                                     for costos_fijos_ano2, costos_variables_ano2, ventas_ano2
                                                     in zip(punto_equilibrio['costos_fijos_ano2'],
                                                            punto_equilibrio['costos_variables_ano2'],
                                                            punto_equilibrio['ventas_ano2'])]
        punto_equilibrio['punto_equilibrio_ano3'] = [costos_fijos_ano3 / (1 - costos_variables_ano3 / ventas_ano3)
                                                     for costos_fijos_ano3, costos_variables_ano3, ventas_ano3
                                                     in zip(punto_equilibrio['costos_fijos_ano3'],
                                                            punto_equilibrio['costos_variables_ano3'],
                                                            punto_equilibrio['ventas_ano3'])]
        punto_equilibrio['punto_equilibrio_ano4'] = [costos_fijos_ano4 / (1 - costos_variables_ano4 / ventas_ano4)
                                                     for costos_fijos_ano4, costos_variables_ano4, ventas_ano4
                                                     in zip(punto_equilibrio['costos_fijos_ano4'],
                                                            punto_equilibrio['costos_variables_ano4'],
                                                            punto_equilibrio['ventas_ano4'])]
        punto_equilibrio['punto_equilibrio_ano5'] = [costos_fijos_ano5 / (1 - costos_variables_ano5 / ventas_ano5)
                                                     for costos_fijos_ano5, costos_variables_ano5, ventas_ano5
                                                     in zip(punto_equilibrio['costos_fijos_ano5'],
                                                            punto_equilibrio['costos_variables_ano5'],
                                                            punto_equilibrio['ventas_ano5'])]
        punto_equilibrio['punto_equilibrio_ano1_porcentaje'] = [punto_equilibrio_ano1 / ventas_ano1
                                                                for punto_equilibrio_ano1, ventas_ano1
                                                                in zip(punto_equilibrio['punto_equilibrio_ano1'],
                                                                       punto_equilibrio['ventas_ano1'])]
        punto_equilibrio['punto_equilibrio_ano2_porcentaje'] = [punto_equilibrio_ano2 / ventas_ano2
                                                                for punto_equilibrio_ano2, ventas_ano2
                                                                in zip(punto_equilibrio['punto_equilibrio_ano2'],
                                                                       punto_equilibrio['ventas_ano2'])]
        punto_equilibrio['punto_equilibrio_ano3_porcentaje'] = [punto_equilibrio_ano3 / ventas_ano3
                                                                for punto_equilibrio_ano3, ventas_ano3
                                                                in zip(punto_equilibrio['punto_equilibrio_ano3'],
                                                                       punto_equilibrio['ventas_ano3'])]
        punto_equilibrio['punto_equilibrio_ano4_porcentaje'] = [punto_equilibrio_ano4 / ventas_ano4
                                                                for punto_equilibrio_ano4, ventas_ano4
                                                                in zip(punto_equilibrio['punto_equilibrio_ano4'],
                                                                       punto_equilibrio['ventas_ano4'])]
        punto_equilibrio['punto_equilibrio_ano5_porcentaje'] = [punto_equilibrio_ano5 / ventas_ano5
                                                                for punto_equilibrio_ano5, ventas_ano5
                                                                in zip(punto_equilibrio['punto_equilibrio_ano5'],
                                                                       punto_equilibrio['ventas_ano5'])]

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # BLOQUE 9: ANALISIS DE RENTABILIDAD
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        analisis_rentabilidad = {'ingresos_ano1': [ingresos_totales_ano1 for ingresos_totales_ano1
                                                   in flujo_efectivo['ingresos_totales_ano1']],
                                 'ingresos_ano2': [ingresos_totales_ano2 for ingresos_totales_ano2
                                                   in flujo_efectivo['ingresos_totales_ano2']],
                                 'ingresos_ano3': [ingresos_totales_ano3 for ingresos_totales_ano3
                                                   in flujo_efectivo['ingresos_totales_ano3']],
                                 'ingresos_ano4': [ingresos_totales_ano4 for ingresos_totales_ano4
                                                   in flujo_efectivo['ingresos_totales_ano4']],
                                 'ingresos_ano5': [ingresos_totales_ano5 for ingresos_totales_ano5
                                                   in flujo_efectivo['ingresos_totales_ano5']],
                                 'costos_ano0': [compra_activo_fijo + compra_activo_diferido + compra_capital_trabajo
                                                 for compra_activo_fijo, compra_activo_diferido, compra_capital_trabajo
                                                 in zip(flujo_efectivo['compra_activo_fijo'],
                                                        flujo_efectivo['compra_activo_diferido'],
                                                        flujo_efectivo['compra_capital_trabajo'])],
                                 'costos_ano1': [costos_totales_ano1 for costos_totales_ano1
                                                 in flujo_efectivo['costos_totales_ano1']],
                                 'costos_ano2': [costos_totales_ano2 for costos_totales_ano2
                                                 in flujo_efectivo['costos_totales_ano3']],
                                 'costos_ano3': [costos_totales_ano3 for costos_totales_ano3
                                                 in flujo_efectivo['costos_totales_ano3']],
                                 'costos_ano4': [costos_totales_ano4 for costos_totales_ano4
                                                 in flujo_efectivo['costos_totales_ano4']],
                                 'costos_ano5': [costos_totales_ano5 for costos_totales_ano5
                                                 in flujo_efectivo['costos_totales_ano5']]}
        analisis_rentabilidad['flujo_efectivo_ano0'] = [costos_ano0 for costos_ano0
                                                        in analisis_rentabilidad['costos_ano0']]
        analisis_rentabilidad['flujo_efectivo_ano1'] = [ingresos_ano1 - costos_ano1
                                                        for ingresos_ano1, costos_ano1
                                                        in zip(analisis_rentabilidad['ingresos_ano1'],
                                                               analisis_rentabilidad['costos_ano1'])]
        analisis_rentabilidad['flujo_efectivo_ano2'] = [ingresos_ano2 - costos_ano2
                                                        for ingresos_ano2, costos_ano2
                                                        in zip(analisis_rentabilidad['ingresos_ano2'],
                                                               analisis_rentabilidad['costos_ano2'])]
        analisis_rentabilidad['flujo_efectivo_ano3'] = [ingresos_ano3 - costos_ano3
                                                        for ingresos_ano3, costos_ano3
                                                        in zip(analisis_rentabilidad['ingresos_ano3'],
                                                               analisis_rentabilidad['costos_ano3'])]
        analisis_rentabilidad['flujo_efectivo_ano4'] = [ingresos_ano4 - costos_ano4
                                                        for ingresos_ano4, costos_ano4
                                                        in zip(analisis_rentabilidad['ingresos_ano4'],
                                                               analisis_rentabilidad['costos_ano4'])]
        analisis_rentabilidad['flujo_efectivo_ano5'] = [ingresos_ano5 - costos_ano5
                                                        for ingresos_ano5, costos_ano5
                                                        in zip(analisis_rentabilidad['ingresos_ano5'],
                                                               analisis_rentabilidad['costos_ano5'])]
        analisis_rentabilidad['tasa_ano0'] = [1 / (1 + 0.1) ** 0]
        analisis_rentabilidad['tasa_ano1'] = [1 / (1 + 0.1) ** 1]
        analisis_rentabilidad['tasa_ano2'] = [1 / (1 + 0.1) ** 2]
        analisis_rentabilidad['tasa_ano3'] = [1 / (1 + 0.1) ** 3]
        analisis_rentabilidad['tasa_ano4'] = [1 / (1 + 0.1) ** 4]
        analisis_rentabilidad['tasa_ano5'] = [1 / (1 + 0.10) ** 5]
        analisis_rentabilidad['ingresos_actualizados_ano1'] = [tasa_ano1 * ingresos_ano1
                                                               for tasa_ano1, ingresos_ano1
                                                               in zip(analisis_rentabilidad['tasa_ano1'],
                                                                      analisis_rentabilidad['ingresos_ano1'])]
        analisis_rentabilidad['ingresos_actualizados_ano2'] = [tasa_ano2 * ingresos_ano2
                                                               for tasa_ano2, ingresos_ano2
                                                               in zip(analisis_rentabilidad['tasa_ano2'],
                                                                      analisis_rentabilidad['ingresos_ano2'])]
        analisis_rentabilidad['ingresos_actualizados_ano3'] = [tasa_ano3 * ingresos_ano3
                                                               for tasa_ano3, ingresos_ano3
                                                               in zip(analisis_rentabilidad['tasa_ano3'],
                                                                      analisis_rentabilidad['ingresos_ano3'])]
        analisis_rentabilidad['ingresos_actualizados_ano4'] = [tasa_ano4 * ingresos_ano4
                                                               for tasa_ano4, ingresos_ano4
                                                               in zip(analisis_rentabilidad['tasa_ano4'],
                                                                      analisis_rentabilidad['ingresos_ano4'])]
        analisis_rentabilidad['ingresos_actualizados_ano5'] = [tasa_ano5 * ingresos_ano5
                                                               for tasa_ano5, ingresos_ano5
                                                               in zip(analisis_rentabilidad['tasa_ano5'],
                                                                      analisis_rentabilidad['ingresos_ano5'])]
        analisis_rentabilidad['egresos_actualizado_ano0'] = [tasa_ano0 * costos_ano0
                                                             for tasa_ano0, costos_ano0
                                                             in zip(analisis_rentabilidad['tasa_ano0'],
                                                                    analisis_rentabilidad['costos_ano0'])]
        analisis_rentabilidad['egresos_actualizados_ano1'] = [tasa_ano1 * costos_ano1
                                                              for tasa_ano1, costos_ano1
                                                              in zip(analisis_rentabilidad['tasa_ano1'],
                                                                     analisis_rentabilidad['costos_ano1'])]
        analisis_rentabilidad['egresos_actualizados_ano2'] = [tasa_ano2 * costos_ano2
                                                              for tasa_ano2, costos_ano2
                                                              in zip(analisis_rentabilidad['tasa_ano2'],
                                                                     analisis_rentabilidad['costos_ano2'])]
        analisis_rentabilidad['egresos_actualizados_ano3'] = [tasa_ano3 * costos_ano3
                                                              for tasa_ano3, costos_ano3
                                                              in zip(analisis_rentabilidad['tasa_ano3'],
                                                                     analisis_rentabilidad['costos_ano3'])]
        analisis_rentabilidad['egresos_actualizados_ano4'] = [tasa_ano4 * costos_ano4
                                                              for tasa_ano4, costos_ano4
                                                              in zip(analisis_rentabilidad['tasa_ano4'],
                                                                     analisis_rentabilidad['costos_ano4'])]
        analisis_rentabilidad['egresos_actualizados_ano5'] = [tasa_ano5 * costos_ano5
                                                              for tasa_ano5, costos_ano5
                                                              in zip(analisis_rentabilidad['tasa_ano5'],
                                                                     analisis_rentabilidad['costos_ano5'])]
        analisis_rentabilidad['total_ingresos'] = [sum(analisis_rentabilidad['ingresos_ano1']
                                                       + analisis_rentabilidad['ingresos_ano2']
                                                       + analisis_rentabilidad['ingresos_ano3']
                                                       + analisis_rentabilidad['ingresos_ano4']
                                                       + analisis_rentabilidad['ingresos_ano5'])]
        analisis_rentabilidad['total_costos'] = [sum(analisis_rentabilidad['costos_ano1']
                                                     + analisis_rentabilidad['costos_ano2']
                                                     + analisis_rentabilidad['costos_ano3']
                                                     + analisis_rentabilidad['costos_ano4']
                                                     + analisis_rentabilidad['costos_ano5'])]
        analisis_rentabilidad['total_flujo_efectivo'] = [sum(analisis_rentabilidad['flujo_efectivo_ano0']
                                                             + analisis_rentabilidad['flujo_efectivo_ano1']
                                                             + analisis_rentabilidad['flujo_efectivo_ano2']
                                                             + analisis_rentabilidad['flujo_efectivo_ano3']
                                                             + analisis_rentabilidad['flujo_efectivo_ano4']
                                                             + analisis_rentabilidad['flujo_efectivo_ano5'])]
        analisis_rentabilidad['total_ingresos_actualizados'] = [sum(analisis_rentabilidad['ingresos_actualizados_ano1']
                                                                    + analisis_rentabilidad['ingresos_actualizados_ano2']
                                                                    + analisis_rentabilidad['ingresos_actualizados_ano3']
                                                                    + analisis_rentabilidad['ingresos_actualizados_ano4']
                                                                    + analisis_rentabilidad['ingresos_actualizados_ano5'])]
        analisis_rentabilidad['total_egresos_actualizados'] = [sum(analisis_rentabilidad['egresos_actualizados_ano1']
                                                                   + analisis_rentabilidad['egresos_actualizados_ano2']
                                                                   + analisis_rentabilidad['egresos_actualizados_ano3']
                                                                   + analisis_rentabilidad['egresos_actualizados_ano4']
                                                                   + analisis_rentabilidad['egresos_actualizados_ano5'])]


        van_tir_bc = {'van': [total_ingresos_actualizados - total_egresos_actualizados
                              for total_ingresos_actualizados, total_egresos_actualizados
                              in zip(analisis_rentabilidad['total_ingresos_actualizados'],
                                     analisis_rentabilidad['total_egresos_actualizados'])],
                      'bc': [total_ingresos_actualizados / total_egresos_actualizados
                             for total_ingresos_actualizados, total_egresos_actualizados
                             in zip(analisis_rentabilidad['total_ingresos_actualizados'],
                                   analisis_rentabilidad['total_egresos_actualizados'])]}


        BC = 0
        VAN = 0
        var_total_ingresos_actualizados = 0
        var_total_egresos_actualizados = 0
        if not BC:
            BC = 'null'
        for x in van_tir_bc['bc']:
            BC = x

        for y in van_tir_bc['van']:
            VAN = y

        for j in analisis_rentabilidad['total_ingresos_actualizados']:
            var_total_ingresos_actualizados = j

        for k in analisis_rentabilidad['total_egresos_actualizados']:
            var_total_egresos_actualizados = k
        var_total_presupuesto_inversion = 0
        for l in total_presupuesto_inversion['total_B1']:
            var_total_presupuesto_inversion = l

        var_memorias_calculo = memorias_calculo['concepto']
        formatted_content = "\n".join(var_memorias_calculo)

        var_memorias_costos = memorias_calculo['costo_insumo']

        # Convertir la lista a una cadena con saltos de línea
        formatted_content_costos_str = '\n'.join(f'${var:.2f}' for var in var_memorias_costos)
        var_memorias_venta = memorias_calculo['precio_venta']
        formatted_content_venta_str = '\n'.join(f'${var:2f}' for var in var_memorias_venta)

        instance = data_corrida_financiera.objects.create(user=user,
                                                          data_activo_fijo=activo_fijo,
                                                          data_activo_diferido=Activo_diferido,
                                                          data_capital_trabajo_mano_obra=capital_trabajo_mano_obra,
                                                          data_capital_trabajo_servicios=capital_trabajo_servicios,
                                                          data_capital_trabajo_servicios_mantto=capital_trabajo_servicios_mantto,
                                                          data_memorias_calculo=memorias_calculo,
                                                          data_total_inversion=total_presupuesto_inversion)
        instance.save()

        return redirect('canvas')


    return render(request, 'corrida_financiera.html')


@login_required
def canvas(request, BC = None, var_total_presupuesto_inversion = None,
           formatted_content = None, formatted_content_costos_str = None,
           formatted_content_venta_str = None):
    try:
        user = request.user
        last = AnswersChatgpt.objects.filter(user=user).last()
        last_name = answers_user.objects.filter(user=user).last()
        proyect_name = last_name.name_e_p
        last_image = GeneratedImage.objects.filter(user=user).last()
        last_logo = LogoProyect.objects.filter(user=user).last()
        last_memorias_calculo = data_corrida_financiera.objects.filter(user=user).last()

        memorias_calculo = last_memorias_calculo.data_memorias_calculo
        inversion = last_memorias_calculo.data_total_inversion

        memorias_concepto = []
        memorias_costo = []
        memorias_venta = []
        total_inversion = []

        for i, j, k in zip(memorias_calculo['concepto'], memorias_calculo['costo_insumo'],
                              memorias_calculo['ventas_semana']):
            memorias_concepto.append(i)
            memorias_costo.append(j)
            memorias_venta.append(k)

        for l in inversion['total_B1']:
            total_inversion.append(l)

        memorias_concepto_print = '\n'.join(memorias_concepto)
        memorias_costo_print = '\n'.join(f'${var:.2f}' for var in memorias_costo)
        memorias_venta_print = '\n'.join(f'${var:.2f}' for var in memorias_venta)
        total_inversion_print = '\n'.join(f'{var:.2f}' for var in total_inversion)

        costos_ingresos = [
            memorias_concepto_print,
            memorias_costo_print,
            memorias_venta_print,
            total_inversion_print
        ]
        print('##################xddd')
        print(memorias_concepto)

        answers_canvas = [
            last.segmento_gpt,
            last.propuesta_gpt,
            last.canales_gpt,
            last.relaciones_gpt,
            last.recursos_gpt,
            last.actividades_gpt,
            last.socios_gpt,
        ]
        images = [
            last_image.segmento_image1,
            last_image.segmento_image2,
            last_image.propuesta_image1,
            last_image.propuesta_image2,
            last_image.canales_image,
            last_image.relaciones_image,
            last_image.recursos_image,
            last_image.actividades_image,
            last_image.socios_image1,
            last_image.socios_image2,
            last_image.ingresos_image,
            last_image.costos_image
        ]
        data = {'respuestas_canvas': answers_canvas,
                'image': images,
                'BC': str(BC),
                'Presupuesto_inversion': str(var_total_presupuesto_inversion),
                'formatted_content': formatted_content,
                'formatted_content_costos_str': formatted_content_costos_str,
                'formatted_content_venta_str': formatted_content_venta_str,
                'logo': last_logo,
                'costos_ingresos': costos_ingresos,
                'nombre': proyect_name}



        return render(request, 'canvas.html',data)

    except AttributeError:
        # Manejo del error
        answers_canvas = []  # O cualquier otra lógica que desees utilizar en caso de error
        proyect_name = None  # O cualquier otro valor o lógica que desees utilizar en caso de error

        return render(request, 'canvas.html', {
            'respuestas_canvas': answers_canvas,
            'nombre': proyect_name
        })
def presupuesto_inversion(request):
    user = request.user
    last_inversion = data_corrida_financiera.objects.filter(user=user).last()
    activo_fijo = last_inversion.data_activo_fijo
    activo_diferido = last_inversion.data_activo_diferido
    capital_trabajo_mano_obra = last_inversion.data_capital_trabajo_mano_obra
    capital_trabajo_servicios = last_inversion.data_capital_trabajo_servicios
    capital_trabajo_servicios_mantto = last_inversion.data_capital_trabajo_servicios_mantto
    inversion_total = last_inversion.data_total_inversion


    #Declaración de variables tipo lista para implementar el objects filter obtenido
    lista_activo_fijo=[]
    activo_fijo_unidad = []
    activo_fijo_cantidad = []
    activo_fijo_costo_unitario =[]
    activo_fijo_montos = []
    activo_fijo_total = []

    lista_activo_diferido = []
    activo_diferido_unidad = []
    activo_diferido_cantidad = []
    activo_diferido_costo_unitario = []
    activo_diferido_montos = []
    activo_diferido_total = []

    lista_capital_mano_obra = []
    capital_mano_obra_cantidad = []
    capital_mano_obra_costo_unitario = []
    capital_mano_obra_montos = []
    capital_mano_obra_total = []

    lista_capital_trabajo_servicios = []
    capital_trabajo_servicios_cantidad = []
    capital_trabajo_servicios_costo_unitario = []
    capital_trabajo_servicios_montos = []
    capital_trabajo_servicios_total = []

    lista_capital_trabjo_servicios_mantto = []
    capital_trabajo_servicios_mantto_cantidad = []
    capital_trabajo_servicios_mantto_costo_unitario = []
    capital_trabajo_servicios_mantto_montos = []
    capital_trabajo_servicios_mantto_total = []

    total_montos = []
    total_inversion = []

    for i, j, k, l,m,n in zip(activo_fijo['concepto'], activo_fijo['unidad'],
                          activo_fijo['cantidad'], activo_fijo['costo_unitario'],
                          activo_fijo['montos'], activo_fijo['total']):
        lista_activo_fijo.append(i)
        activo_fijo_unidad.append(j)
        activo_fijo_cantidad.append(k)
        activo_fijo_costo_unitario.append(l)
        activo_fijo_montos.append(m)
        activo_fijo_total.append(n)

    lista_activo_fijo_print = '\n'.join(lista_activo_fijo)
    activo_fijo_unidad_print="\n".join(activo_fijo_unidad)
    activo_fijo_cantidad_print = "\n".join(f'{var}' for var in activo_fijo_cantidad)
    activo_fijo_costo_unitario_print = '\n'.join(f'${var:.2f}' for var in activo_fijo_costo_unitario)
    activo_fijo_montos_print = '\n'.join(f'${var:.2f}' for var in activo_fijo_montos)
    activo_fijo_total_print = '\n'.join(f'${var:.2f}' for var in activo_fijo_total)

    for i,j,k,l,m,n in zip(activo_diferido['concepto'], activo_fijo['unidad'],
                                       activo_fijo['cantidad'], activo_diferido['costo_unitario'],
                                       activo_diferido['montos'], activo_diferido['total']):
        lista_activo_diferido.append(i)
        activo_diferido_unidad.append(j)
        activo_diferido_cantidad.append(k)
        activo_diferido_costo_unitario.append(l)
        activo_diferido_montos.append(m)
        activo_diferido_total.append(n)

    lista_activo_diferido_print='\n'.join(lista_activo_diferido)
    activo_diferido_unidad_print = '\n'.join(activo_diferido_unidad)
    activo_diferido_cantidad_print = '\n'.join(f'{var}' for var in activo_diferido_cantidad)
    activo_diferido_costo_unitario_print = '\n'.join(f'${var:.2f}' for var in activo_diferido_costo_unitario)
    activo_diferido_montos_print = '\n'.join(f'${var:.2f}' for var in activo_diferido_montos)
    activo_diferido_total_print = '\n'.join(f'${var:.2f}' for var in activo_diferido_total)

    for i,j,k,l,m in zip(capital_trabajo_mano_obra['unidad'],
                           capital_trabajo_mano_obra['cantidad'],
                           capital_trabajo_mano_obra['costo_unitario'],
                           capital_trabajo_mano_obra['montos'],
                           capital_trabajo_mano_obra['total']):
        lista_capital_mano_obra.append(i)
        capital_mano_obra_cantidad.append(j)
        capital_mano_obra_costo_unitario.append(k)
        capital_mano_obra_montos.append(l)
        capital_mano_obra_total.append(m)

    capital_mano_obra_unidad_print = '\n'.join(lista_capital_mano_obra)
    capital_mano_obra_cantidad_print = '\n'.join(f'{var}' for var in capital_mano_obra_cantidad)
    capital_mano_obra_costo_unitario_print = '\n'.join(f'${var:.2f}' for var in capital_mano_obra_costo_unitario)
    capital_mano_obra_montos_print = '\n'.join(f'${var:.2f}' for var in capital_mano_obra_montos)
    capital_mano_obra_total_print = '\n'.join(f'${var:.2f}' for var in capital_mano_obra_total)

    for i,j,k,l,m in zip(capital_trabajo_servicios['unidad'],
                         capital_trabajo_servicios['cantidad'],
                         capital_trabajo_servicios['costo_unitario'],
                         capital_trabajo_servicios['montos'],
                         capital_trabajo_servicios['total']):

        lista_capital_trabajo_servicios.append(i)
        capital_trabajo_servicios_cantidad.append(j)
        capital_trabajo_servicios_costo_unitario.append(k)
        capital_trabajo_servicios_montos.append(l)
        capital_trabajo_servicios_total.append(m)

    capital_trabajo_servicios_unidad_print = '\n'.join(lista_capital_trabajo_servicios)
    capital_trabajo_servicios_cantidad_print = '\n'.join(f'{var}' for var in capital_trabajo_servicios_cantidad)
    capital_trabajo_servicios_costo_unitario_print = '\n'.join(f'${var:.2f}' for var in capital_trabajo_servicios_costo_unitario)
    capital_trabajo_servicios_montos_print = '\n'.join(f'${var:.2f}' for var in capital_trabajo_servicios_montos)
    capital_trabajo_servicios_tota_print = '\n'.join(f'${var:.2f}' for var in capital_trabajo_servicios_total)

    for i,j,k,l,m in zip(capital_trabajo_servicios_mantto['unidad'],
                         capital_trabajo_servicios_mantto['cantidad'],
                         capital_trabajo_servicios_mantto['costo_unitario'],
                         capital_trabajo_servicios_mantto['montos'],
                         capital_trabajo_servicios_mantto['total']):

        lista_capital_trabjo_servicios_mantto.append(i)
        capital_trabajo_servicios_mantto_cantidad.append(j)
        capital_trabajo_servicios_mantto_costo_unitario.append(k)
        capital_trabajo_servicios_mantto_montos.append(l)
        capital_trabajo_servicios_mantto_total.append(m)

    capital_trabajo_servicios_mantto_unidad_print = '\n'.join(lista_capital_trabjo_servicios_mantto)
    capital_trabajo_servicios_mantto_cantidad_print = '\n'.join(f'{var}' for var in capital_trabajo_servicios_mantto_cantidad)
    capital_trabajo_servicios_mantto_costo_unitario_print = '\n'.join(f'${var:.2f}' for var in
                                                                      capital_trabajo_servicios_mantto_costo_unitario)
    capital_trabajo_servicios_mantto_montos_print = '\n'.join(f'${var:.2f}' for var in capital_trabajo_servicios_mantto_montos)
    capital_trabajo_servicios_mantto_total_print = '\n'.join(f'${var:.2f}' for var in capital_trabajo_servicios_mantto_total)

    for i, j in zip(inversion_total['total_monto'], inversion_total['total_B1']):
        total_montos.append(i)
        total_inversion.append(j)
    total_montos_print = '\n'.join(f'${var:.2f}' for var in total_montos)
    total_inversion_print = '\n'.join(f'${var:.2f}' for var in total_inversion)


    listas_print = {'activo_fijo_concepto': lista_activo_fijo_print,
                    'activo_fijo_unidad': activo_fijo_unidad_print,
                    'activo_fijo_cantidad': activo_fijo_cantidad_print,
                    'activo_fijo_costo_unitario': activo_fijo_costo_unitario_print,
                    'activo_fijo_montos': activo_fijo_montos_print,
                    'activo_fijo_total': activo_fijo_total_print,

                    'activo_diferido_concepto': lista_activo_diferido_print,
                    'activo_diferido_unidad': activo_diferido_unidad_print,
                    'activo_diferido_cantidad': activo_diferido_cantidad_print,
                    'activo_diferido_costo_unitario': activo_diferido_costo_unitario_print,
                    'activo_diferido_montos': activo_diferido_montos_print,
                    'activo_diferido_total': activo_diferido_total_print,

                    'mano_obra_unidad': capital_mano_obra_unidad_print,
                    'mano_obra_cantidad': capital_mano_obra_cantidad_print,
                    'mano_obra_costo_unitario': capital_mano_obra_costo_unitario_print,
                    'mano_obra_montos': capital_mano_obra_montos_print,
                    'mano_obra_total': capital_mano_obra_total_print,

                    'trabajo_servicios_unidad': capital_trabajo_servicios_unidad_print,
                    'trabajo_servicios_cantidad': capital_trabajo_servicios_cantidad_print,
                    'trabajo_servicios_costo_unitario': capital_trabajo_servicios_costo_unitario_print,
                    'trabajo_servicios_montos': capital_trabajo_servicios_montos_print,
                    'trabajo_servicios_total': capital_trabajo_servicios_tota_print,

                    'servicios_mantto_unidad': capital_trabajo_servicios_mantto_unidad_print,
                    'servicios_mantto_cantidad': capital_trabajo_servicios_mantto_cantidad_print,
                    'servicios_mantto_costo_unitario': capital_trabajo_servicios_mantto_costo_unitario_print,
                    'servicios_mantto_montos': capital_trabajo_servicios_mantto_montos_print,
                    'servicios_mantto_total': capital_trabajo_servicios_mantto_total_print,

                    'total_montos': total_montos_print,
                    'total_inversion': total_inversion_print
                    }
    return render(request, 'presupuesto_inversion.html', {'list': listas_print})
