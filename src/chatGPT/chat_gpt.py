import os
import openai
from dotenv import load_dotenv
import sys

# cargar las variables de entorno desde el archivo .env
load_dotenv()

# configurar la apikey
openai.api_key = os.getenv("OPENAI_API_KEY")

role_system = {"role": "system","content": ""}
buffer_messages = [role_system]

def respuesta_chat_gpt():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=buffer_messages,
            temperature=1,
            max_tokens=50
        )

        return response.choices[0].message.content
    except ValueError as error:
        print(error)

conversacion = False

if (len(sys.argv) > 1 and sys.argv[1] == "--convers"):
    conversacion = True
    print("MODO CONVERSACION")

print("ingrese una consulta no vacia o ingrese 'salir' si quiere abandonar")

while True:
    try:
        consulta = input("You: ")

        if consulta:
            ultima_consulta = consulta

            if (consulta == "salir"):
                break
            elif (consulta == "\033[A"):         # "\033[A" mover el cursor una linea para arriba con la flecha para arriba
                consulta = ultima_consulta

            if conversacion:  # cuando esta en modo conversacion
                buffer_messages.append({"role": "user", "content": consulta})

                try:
                    respuesta = respuesta_chat_gpt()
                    buffer_messages.append({"role": "assistant", "content": respuesta})                                        
                    print("chatGPT:", respuesta)
                except ValueError as error:
                    print(error)
            else:  # cuando NO esta en modo conversacion
                buffer_messages = [role_system, {"role": "user", "content": consulta}]
                    
                try:
                    respuesta = respuesta_chat_gpt()
                    print("chatGPT:", respuesta)
                except ValueError as error:
                    print(error)
        else:
            print("ingresa una consulta válida")
    except ValueError as error:
        print(error)