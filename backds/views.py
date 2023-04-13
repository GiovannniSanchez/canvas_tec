from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import answers_user
from django.http import HttpResponse
import openai

def about(request):
    return render(request,'about.html')
@login_required
def prueba(request):
    #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
    openai.api_key = "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"

    # Contexto del asistente
    variable='anime'
    messages = [{"role": "system", "content": "Eres un experto en modelos de negocio"+ 'y'+ variable}]

    parte1='dame la lista de pasos'
    parte2='para crear un modelo de:'
    parte3='negocio'
    contenido =parte1+parte2+parte3


    messages.append({"role": "user", "content": contenido})
    respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=1000)
    contenido_respuesta = respuesta.choices[0].message.content
    messages.append({"role": "assistant", "content": contenido_respuesta})
    return render(request,'chatgpt.html',{
        'contenido_respuesta':contenido_respuesta,
        'contenido':contenido
    })
@login_required
def formulario(request):
    return render(request,'formulario.html')

def test01(request):
        answers= answers_user.objects.get(id=1)
        data=(answers.answer1, answers.answer2,
              answers.answer3, answers.answer4,
              answers.answer5, answers.answer6,
              answers.answer7)
        return render(request, "test01.html",{
            'answers': data
        })
@login_required
def canvas(request):
    Problema='este es'
    variable2='un texto de prueba'
    variable3='prueba respuesta xddd'
    return  render(request, 'canvas.html',{
        'texto1': Problema,
        'texto2': variable2,
        'texto3': variable3
    })

