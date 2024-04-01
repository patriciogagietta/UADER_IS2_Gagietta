import os
import openai
from dotenv import load_dotenv

# cargar las variables de entorno desde el archivo .env
load_dotenv()

# configurar la apikey
openai.api_key = os.getenv("OPENAI_API_KEY")

def respuesta_chat_gpt(consulta):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "user", "content": consulta}
        ],
        temperature=1,
        max_tokens=20
    )
    return response.choices[0].message.content


while True:
    consulta = input("You: ")

    if consulta:
        respuesta = respuesta_chat_gpt(consulta)

        print("chatGPT:", respuesta)
    else:
        print("Por favor, ingresa una consulta válida.")