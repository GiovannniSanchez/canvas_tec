from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import answers_user, AnswersChatgpt
from .forms import RegisterAnswer
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import openai
import time


def about(request):
    return render(request, 'about.html')


@login_required
def prueba(request):
    user = request.user
    answers = answers_user.objects.filter(user=user)
    answers_list = []
    for a in answers:
        answers_list.append(a.answer1)
        answers_list.append(a.answer2)
        answers_list.append(a.answer3)
        answers_list.append(a.answer4)
        answers_list.append(a.answer5)
        answers_list.append(a.answer6)
        answers_list.append(a.answer7)
        answers_list.append(a.answer8)
        answers_list.append(a.answer9)
        answers_list.append(a.answer10)

        print(len(answers_list))
    # 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
    openai.api_key = "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"

    # Contexto del asistente
    messages = [{"role": "system", "content": "Eres un experto en modelos de negocio"}]

    preguntas = [
        '¿Que vas a ofrecer al mercado?: ',
        '¿Sabes como elaborarlo?: ',
        '¿Como te daras a conocer a tus clientes?: ',
        '¿Que problema resuelve?: ',
        '¿Cuanto va a costar?: ',
        '¿Como lo vas a vender?: ',
        '¿A quien se lo vas a vender?: ',
        '¿Existen alternativas a tu producto o servicio?: ',
        '¿Que hace a tu producto diferente a los demas?: ',
        '¿Cual es la razon por la cual los clientes comprarán lo que ofreces?: '
    ]

    prompt_default1 = 'dado un formato canvas que contiene 4 aspectos clave los cuales son el ¿quien?,¿que?,¿como? y ¿cuanto? y se ' \
                      'estos contienen a su vez una serie de puntos clave:' \
                      'en el aspecto ¿Quien? se encuentran los puntos de: Segmento de clientes, ventaja diferencial y canales.' \
                      'En el aspecto ¿Que? se encuentra el punto: Propuesta unica de valor.' \
                      'En el aspecto ¿Como? se encuentran los puntos: problema, solución y metricas.' \
                      'Y en el aspecto ¿Cuanto se encuentran los puntos: Estructura de costes y flujo de ingresos.' \
                      'Ahora segun la estrctura anterior puedes darme el segmento de clientes segun tu interpretacion como experto en modelo de negocios' \
                      'haciendo referencia a las siguientes preguntas con sus respectivas respuestas y me lo puedes dar en un formato corto y en forma de lista en caso de llevar' \
                      'varios puntos?: '

    prompt_default2='dado un formato canvas que contiene 4 aspectos clave los cuales son el ¿quien?,¿que?,¿como? y ¿cuanto? y se ' \
                      'estos contienen a su vez una serie de puntos clave:' \
                      'en el aspecto ¿Quien? se encuentran los puntos de: Segmento de clientes, ventaja diferencial y canales.' \
                      'En el aspecto ¿Que? se encuentra el punto: Propuesta unica de valor.' \
                      'En el aspecto ¿Como? se encuentran los puntos: problema, solución y metricas.' \
                      'Y en el aspecto ¿Cuanto se encuentran los puntos: Estructura de costes y flujo de ingresos.' \
                      'Ahora segun la estrctura anterior puedes darme el punto "problema" del aspecto ¿Como? segun tu interpretacion como experto en modelo de negocios ' \
                      'haciendo referencia a las siguientes preguntas cons sus respectivas respuestas y me lo puedes dar en un formato corto y en forma de lista en caso de llevar' \
                      'varios puntos?: '

    prompt_default3='dado un formato canvas que contiene 4 aspectos clave los cuales son el ¿quien?,¿que?,¿como? y ¿cuanto? y se ' \
                      'estos contienen a su vez una serie de puntos clave:' \
                      'en el aspecto ¿Quien? se encuentran los puntos de: Segmento de clientes, ventaja diferencial y canales.' \
                      'En el aspecto ¿Que? se encuentra el punto: Propuesta unica de valor.' \
                      'En el aspecto ¿Como? se encuentran los puntos: problema, solución y metricas.' \
                      'Y en el aspecto ¿Cuanto se encuentran los puntos: Estructura de costes y flujo de ingresos.' \
                      'Ahora segun la estrctura anterior puedes darme el punto "propuesta unica de valor" segun tu interpretacion como experto en modelo de negocios ' \
                      'haciendo referencia a las siguientes preguntas con sus respectivas y me lo puedes dar en un formato corto y en forma de lista en caso de llevar' \
                      'varios puntos?: '

    prompt_default4='dado un formato canvas que contiene 4 aspectos clave los cuales son el ¿quien?,¿que?,¿como? y ¿cuanto? y se ' \
                      'estos contienen a su vez una serie de puntos clave:' \
                      'en el aspecto ¿Quien? se encuentran los puntos de: Segmento de clientes, ventaja diferencial y canales.' \
                      'En el aspecto ¿Que? se encuentra el punto: Propuesta unica de valor.' \
                      'En el aspecto ¿Como? se encuentran los puntos: problema, solución y metricas.' \
                      'Y en el aspecto ¿Cuanto se encuentran los puntos: Estructura de costes y flujo de ingresos.' \
                      'Ahora segun la estrctura anterior puedes darme el punto "solución" segun tu interpretacion como experto en modelo de negocios ' \
                      'haciendo referencia a las siguientes preguntas con sus respectivas respuestas y me lo puedes dar en un formato corto y en forma de lista en caso de llevar' \
                      'varios puntos?: '

    prompt_default5='dado un formato canvas que contiene 4 aspectos clave los cuales son el ¿quien?,¿que?,¿como? y ¿cuanto? y se ' \
                      'estos contienen a su vez una serie de puntos clave:' \
                      'en el aspecto ¿Quien? se encuentran los puntos de: Segmento de clientes, ventaja diferencial y canales.' \
                      'En el aspecto ¿Que? se encuentra el punto: Propuesta unica de valor.' \
                      'En el aspecto ¿Como? se encuentran los puntos: problema, solución y metricas.' \
                      'Y en el aspecto ¿Cuanto se encuentran los puntos: Estructura de costes y flujo de ingresos.' \
                      'Ahora segun la estrctura anterior puedes darme el punto "canales" segun tu interpretacion como experto en modelo de negocios ' \
                      'haciendo referencia a las siguientes preguntas con sus respectivas respuestas y me lo puedes dar en un formato corto y en forma de lista en caso de llevar' \
                      'varios puntos?: '

    prompt_default6='dado un formato canvas que contiene 4 aspectos clave los cuales son el ¿quien?,¿que?,¿como? y ¿cuanto? y se ' \
                      'estos contienen a su vez una serie de puntos clave:' \
                      'en el aspecto ¿Quien? se encuentran los puntos de: Segmento de clientes, ventaja diferencial y canales.' \
                      'En el aspecto ¿Que? se encuentra el punto: Propuesta unica de valor.' \
                      'En el aspecto ¿Como? se encuentran los puntos: problema, solución y metricas.' \
                      'Y en el aspecto ¿Cuanto se encuentran los puntos: Estructura de costes y flujo de ingresos.' \
                      'Ahora segun la estrctura anterior puedes darme el punto "flujo de ingresos" segun tu interpretacion como experto en modelo de negocios ' \
                      'haciendo referencia a las siguientes preguntas con sus respectivas respuestas y me lo puedes dar en un formato corto y en forma de lista en caso de llevar' \
                      'varios puntos?: '

    prompt_default7='dado un formato canvas que contiene 4 aspectos clave los cuales son el ¿quien?,¿que?,¿como? y ¿cuanto? y se ' \
                      'estos contienen a su vez una serie de puntos clave:' \
                      'en el aspecto ¿Quien? se encuentran los puntos de: Segmento de clientes, ventaja diferencial y canales.' \
                      'En el aspecto ¿Que? se encuentra el punto: Propuesta unica de valor.' \
                      'En el aspecto ¿Como? se encuentran los puntos: problema, solución y metricas.' \
                      'Y en el aspecto ¿Cuanto se encuentran los puntos: Estructura de costes y flujo de ingresos.' \
                      'Ahora segun la estrctura anterior puedes darme el punto "estructura de costes" segun tu interpretacion como experto en modelo de negocios ' \
                      'haciendo referencia a las siguientes preguntas con sus respectivas respuestas y me lo puedes dar en un formato corto y en forma de lista en caso de llevar' \
                      'varios puntos?: '

    prompt_default8='dado un formato canvas que contiene 4 aspectos clave los cuales son el ¿quien?,¿que?,¿como? y ¿cuanto? y se ' \
                      'estos contienen a su vez una serie de puntos clave:' \
                      'en el aspecto ¿Quien? se encuentran los puntos de: Segmento de clientes, ventaja diferencial y canales.' \
                      'En el aspecto ¿Que? se encuentra el punto: Propuesta unica de valor.' \
                      'En el aspecto ¿Como? se encuentran los puntos: problema, solución y metricas.' \
                      'Y en el aspecto ¿Cuanto se encuentran los puntos: Estructura de costes y flujo de ingresos.' \
                      'Ahora segun la estrctura anterior puedes darme el punto "metricas" segun tu interpretacion como experto en modelo de negocios ' \
                      'haciendo referencia a las siguientes preguntas con sus respectivas respuestas y me lo puedes dar en un formato corto y en forma de lista en caso de llevar' \
                      'varios puntos?: '

    prompt_default9='dado un formato canvas que contiene 4 aspectos clave los cuales son el ¿quien?,¿que?,¿como? y ¿cuanto? y se ' \
                      'estos contienen a su vez una serie de puntos clave:' \
                      'en el aspecto ¿Quien? se encuentran los puntos de: Segmento de clientes, ventaja diferencial y canales.' \
                      'En el aspecto ¿Que? se encuentra el punto: Propuesta unica de valor.' \
                      'En el aspecto ¿Como? se encuentran los puntos: problema, solución y metricas.' \
                      'Y en el aspecto ¿Cuanto se encuentran los puntos: Estructura de costes y flujo de ingresos.' \
                      'Ahora segun la estrctura anterior puedes darme el punto "ventaja diferencial" segun tu interpretacion como experto en modelo de negocios ' \
                      'haciendo referencia a las siguientes preguntas con sus respectivas respuestas y me lo puedes dar en un formato corto y en forma de lista en caso de llevar' \
                      'varios puntos?: '



    preg_resp = '\n'.join([
        f"{preguntas[i]}{str(answers_list[i])}"
        for i in range(len(preguntas))
    ])
#////////////////////////////////////////////////////////////////////////////////////////
    contenido = prompt_default1+preg_resp


    messages.append({"role": "user", "content": contenido})
    respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=100)
    contenido_respuesta = respuesta.choices[0].message.content
    messages.append({"role": "assistant", "content": contenido_respuesta})
     #Guardar la respuesta en la base de datos

    #///////////////////////////////////////////////////////////////////////////////////////////
    contenido1 = prompt_default2 + preg_resp

    messages.append({"role": "user", "content": contenido1})
    respuesta1 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=100)
    contenido_respuesta1 = respuesta1.choices[0].message.content
    messages.append({"role": "assistant", "content": contenido_respuesta1})
    # Guardar la respuesta en la base de datos

    #////////////////////////////////////////////////////////////////////////////////////////////////////

    contenido2 = prompt_default3 + preg_resp

    messages.append({"role": "user", "content": contenido2})
    respuesta2 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=100)
    contenido_respuesta2 = respuesta2.choices[0].message.content
    messages.append({"role": "assistant", "content": contenido_respuesta2})
    # Guardar la respuesta en la base de datos

    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    """
    contenido3 = prompt_default4 + preg_resp

    messages.append({"role": "user", "content": contenido3})
    respuesta3 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=100)
    contenido_respuesta3 = respuesta3.choices[0].message.content
    messages.append({"role": "assistant", "content": contenido_respuesta3})
    # Guardar la respuesta en la base de datos

    #/////////////////////////////////////////////////////////////////////////////////////////////////////7
    contenido4 = prompt_default5 + preg_resp

    messages.append({"role": "user", "content": contenido4})
    respuesta4 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=100)
    contenido_respuesta4 = respuesta4.choices[0].message.content
    messages.append({"role": "assistant", "content": contenido_respuesta4})
    # Guardar la respuesta en la base de datos

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////
    contenido5 = prompt_default6 + preg_resp

    messages.append({"role": "user", "content": contenido5})
    respuesta5 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=100)
    contenido_respuesta5 = respuesta5.choices[0].message.content
    messages.append({"role": "assistant", "content": contenido_respuesta5})
    # Guardar la respuesta en la base de datos

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////
    contenido6 = prompt_default7 + preg_resp

    messages.append({"role": "user", "content": contenido6})
    respuesta6 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=100)
    contenido_respuesta6 = respuesta6.choices[0].message.content
    messages.append({"role": "assistant", "content": contenido_respuesta6})
    # Guardar la respuesta en la base de datos

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    contenido7 = prompt_default7 + preg_resp

    messages.append({"role": "user", "content": contenido7})
    respuesta7 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=100)
    contenido_respuesta7 = respuesta7.choices[0].message.content
    messages.append({"role": "assistant", "content": contenido_respuesta7})
    # Guardar la respuesta en la base de datos
    time.sleep(25)
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////
    contenido8 = prompt_default7 + preg_resp

    messages.append({"role": "user", "content": contenido8})
    respuesta8 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=100)
    contenido_respuesta8 = respuesta8.choices[0].message.content
    messages.append({"role": "assistant", "content": contenido_respuesta8})
    # Guardar la respuesta en la base de datos"""
    answer_chat = AnswersChatgpt.objects.create(user=user,
                                                cliente_ideal=contenido_respuesta,
                                                problema=contenido_respuesta1)
    answer_chat.save()
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////

    return redirect('canvas')

@login_required
def formulario(request):
    if request.method == 'GET':
        return render(request, 'formulario.html', {'form': RegisterAnswer()})
    else:

        user_id = request.user.id
        answers_user.objects.create(answer1=request.POST['answer1'],
                                    answer2=request.POST['answer2'],
                                    answer3=request.POST['answer3'],
                                    answer4=request.POST['answer4'],
                                    answer5=request.POST['answer5'],
                                    answer6=request.POST['answer6'],
                                    answer7=request.POST['answer7'],
                                    answer8=request.POST['answer8'],
                                    answer9=request.POST['answer9'],
                                    answer10=request.POST['answer10'], user_id=user_id)
        return redirect('About')


@login_required
def test01(request):
    user = request.user
    answers = answers_user.objects.filter(user=user)
    return render(request, 'test01.html',{'respuestas':answers})


@login_required
def canvas(request):
    user= request.user
    answers_canvas=AnswersChatgpt.objects.filter(user=user)


    return render(request, 'canvas.html',{'respuestas_canvas':answers_canvas})
