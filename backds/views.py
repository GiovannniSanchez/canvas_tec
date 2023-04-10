from django.shortcuts import render
from django.http import HttpResponse
import openai


def table(request):
    return render(request, 'table.html')

def index(request):
    title= 'Hola desde python'
    return render(request,'index.html',{
        'title': title
    })

def hello(request):
    return HttpResponse('<h1>Hello world</h1>')

def about(request):
    return render(request,'about.html')

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

def formulario(request):
    return render(request,'formulario.html')

def test01(request):
        return render(request, "test01.html")

