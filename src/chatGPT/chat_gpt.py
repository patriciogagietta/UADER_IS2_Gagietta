"""
Este modulo proporciona una implementacion de chat usando el modelo gpt-3.5-turbo-0125 de openAI,
permite generar respuestas a partir de consultas.
"""

import sys
import os
import openai
from dotenv import load_dotenv

# cargar las variables de entorno desde el archivo .env
load_dotenv()

# configurar la apikey
openai.api_key = os.getenv("OPENAI_API_KEY")

role_system = {"role": "system","content": ""}
buffer_messages = [role_system]

def respuesta_chat_gpt():
    """Esta funcion envía una solicitud utilizando la api key de openIA
    para obtener una respuesta a partir de un historial de mensajes de conversación o de una consulta"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",  # version que se usara
            messages=buffer_messages,  # historial de mensajes
            temperature=1,   # controla la aleatoriedad en la generación de respuestas
            max_tokens=50,   # establece el máximo de tokens que puede tener la respuesta
            frequency_penalty=0,   # ajusta la probabilidad de que se repitan palabras o frases en la respuesta
            presence_penalty=0   # ajusta la probabilidad de que se incluyan palabras raras
        )

        return response.choices[0].message.content #retorna el contenido del mensaje ingresado por el usuario
    except ValueError as value_error:
        print(value_error)
        return None

CONVERSACION = False

# verifica si se ingreso algun argumento y si ese es "--convers" para iniciar la conversacion con chatgpt
if (len(sys.argv) > 1 and sys.argv[1] == "--convers"):
    CONVERSACION = True
    print("MODO CONVERSACION")

print("ingrese una consulta no vacia o ingrese 'salir' si quiere abandonar")

# ciclo que permite al usuario interactuar con chatgpt
while True:
    try:
        consulta = input("You: ")

        if consulta:
            # guarda la ultima consulta ingresada por el usuario
            ultima_consulta = consulta

            if consulta == "salir":
                break

            if consulta == "\033[A":         # "\033[A" mover el cursor una linea para arriba con la flecha para arriba
                consulta = ultima_consulta

            if CONVERSACION:  # cuando esta en modo conversacion
                buffer_messages.append({"role": "user", "content": consulta})#guarda la consulta en el buffer con las anteriores
                try:
                    # obtiene la respuesta de chatgpt y la muestra
                    respuesta = respuesta_chat_gpt()
                    buffer_messages.append({"role": "assistant", "content": respuesta})#guarda la respuesta de chatgpt en el buffer con las anteriores usando el role assistent
                    print("chatGPT:", respuesta)
                except ValueError as value_error:
                    print(value_error)
            else:  # cuando NO esta en modo conversacion
                buffer_messages = [role_system, {"role": "user", "content": consulta}]
                try:
                    # obtiene la respuesta de chatgpt y la muestra
                    respuesta = respuesta_chat_gpt()
                    print("chatGPT:", respuesta)
                except ValueError as value_error:
                    print(value_error)
        else:
            print("ingresa una consulta válida")
    except ValueError as value_error:
        print(value_error)
