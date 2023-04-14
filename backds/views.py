from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import answers_user
from .forms import RegisterAnswer
from django.http import HttpResponse,JsonResponse
import openai


def about(request):
    return render(request, 'about.html')


@login_required
def prueba(request):
    user = request.user
    answers = answers_user.objects.filter(user=user)
    answers_list=[]
    for a in answers:
        answers_list.append(a)

    # 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
    openai.api_key = "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"

    # Contexto del asistente
    variable = 'anime'
    messages = [{"role": "system", "content": "Eres un experto en modelos de negocio" }]

    parte1 = str(answers_list[0])
    parte2 = 'para crear un modelo de:'
    parte3 = 'negocio'
    contenido = parte1

    messages.append({"role": "user", "content": contenido})
    respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=1000)
    contenido_respuesta = respuesta.choices[0].message.content
    messages.append({"role": "assistant", "content": contenido_respuesta})
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
   return render(request,'test01.html')


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
