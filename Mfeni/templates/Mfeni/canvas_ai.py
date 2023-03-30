import whisper
import openai
import sounddevice as sd

"""
# Define los parámetros de grabación
duracion = 5  # Duración de la grabación en segundos
frecuencia_muestreo = 44100  # Frecuencia de muestreo en Hz

# Inicia la grabación
grabacion = sd.rec(int(duracion * frecuencia_muestreo), samplerate=frecuencia_muestreo, channels=2)

# Espera a que la grabación se complete
sd.wait()

#Generar el texto de la grabación y guardarla en la variable texto
texto = whisper.audio_to_text(grabacion, frecuencia_muestreo)
print(texto)
"""
"""
# Reproduce la grabación
sd.play(grabacion, samplerate=frecuencia_muestreo)
sd.wait()"""


openai.api_key = "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"

#Contexto del asistente

messages = [{"role": "system", "content": "Eres un experto en anime"}]

while True:
    contenido = input("\nHola, como puedo ayudarte?...\n")
    
    if contenido =="salir":
        break
    messages.append({"role": "user", "content": contenido})
    
    respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages, max_tokens=100)
    
    contenido_respuesta=respuesta.choices[0].message.content
    
    messages.append({"role": "assistant", "content": contenido_respuesta})
    
    print("\n", contenido_respuesta)
    
    
    