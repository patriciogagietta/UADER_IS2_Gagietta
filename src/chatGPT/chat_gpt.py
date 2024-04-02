import os
import openai
from dotenv import load_dotenv
import sys

# cargar las variables de entorno desde el archivo .env
load_dotenv()

# configurar la apikey
openai.api_key = os.getenv("OPENAI_API_KEY")

def respuesta_chat_gpt(consulta):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "user", "content": consulta}
            ],
            temperature=1,
            max_tokens=20
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
            if (consulta == "salir"):
                break
            elif (consulta == "\033[A"):         # "\033[A" mover el cursor una linea para arriba con la flecha para arriba
                consulta = ultima_consulta
            else:
                ultima_consulta = consulta
                
            try:
                respuesta = respuesta_chat_gpt(consulta)
                print("chatGPT:", respuesta)
            except ValueError as error:
                print(error)
        else:
            print("ingresa una consulta válida")
    except ValueError as error:
        print(error)