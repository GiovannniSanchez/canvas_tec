from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import answers_user, AnswersChatgpt
from .forms import RegisterAnswer
from django.http import HttpResponse, JsonResponse
import openai


def about(request):
    return render(request, 'about.html')


@login_required
def prueba(request):
    user = request.user
    answers = answers_user.objects.filter(user=user)
    answers_user_instance = answers_user.objects.get(user=user)
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
                      'haciendo referencia a las siguientes preguntas y me lo puedes dar en un formato corto y en forma de lista en caso de llevar' \
                      'varios puntos?: '

    preg_resp = '\n'.join([
        f"{preguntas[i]}{str(answers_list[i])}"
        for i in range(len(preguntas))
    ])

    contenido = prompt_default1+preg_resp


    messages.append({"role": "user", "content": contenido})
    respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=1000)
    contenido_respuesta = respuesta.choices[0].message.content
    messages.append({"role": "assistant", "content": contenido_respuesta})
    # Guardar la respuesta en la base de datos
    answer_chat = AnswersChatgpt(user=user, respuesta=contenido_respuesta)
    answer_chat.save()

    return render(request, 'chatgpt.html', {
        'contenido_respuesta': contenido_respuesta,
        'contenido': contenido
    })


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
    Problema = 'este es'
    variable2 = 'un texto de prueba'
    variable3 = 'prueba respuesta xddd'
    return render(request, 'canvas.html', {
        'texto1': Problema,
        'texto2': variable2,
        'texto3': variable3
    })
