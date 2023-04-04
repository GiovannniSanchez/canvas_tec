from django.shortcuts import render
from django.http import HttpResponse
import openai


def index(request):
    return render(request, 'Mfeni/index.html')

def Chatgpt(request):
    openai.api_key = "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"


    # Contexto del asistente

    messages = [{"role": "system", "content": "Eres un experto en inteligencia artificial"}]

    while True:
        contenido = 'Que es la inteligencia artificial?'

        if contenido == "salir":
            break
    messages.append({"role": "user", "content": contenido})

    respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=1000)

    contenido_respuesta = respuesta.choices[0].message.content

    messages.append({"role": "assistant", "content": contenido_respuesta})

    return render(request, contenido_respuesta)
