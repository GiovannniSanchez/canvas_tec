from django.shortcuts import render
from django.http import HttpResponse
import openai


def table(request):
    return render(request, 'backds/table.html')

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
    openai.api_key = "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"

    # Contexto del asistente

    messages = [{"role": "system", "content": "Eres un experto en modelos de negocio y mercadotecnia"}]


    contenido =("dame la lista de pasos para crear un modelo de negocio")


    messages.append({"role": "user", "content": contenido})
    respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=1000)
    contenido_respuesta = respuesta.choices[0].message.content
    messages.append({"role": "assistant", "content": contenido_respuesta})
    return render(request,'chatgpt.html',{
        'contenido_respuesta':contenido_respuesta
    })

