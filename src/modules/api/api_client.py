from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api = os.getenv("OPENAI_API_KEY")
print(api)
client = OpenAI(api_key=api)


# Publicar en BlueSky (ejemplo)
def generar_texto_post():
    # Generar contenido
    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {
                "role": "system",
                "content": "Generas post cortos sobre Ingenieria de Datos y programacion web. Tu función es contar tu día a día en ingenieria de Datos y programación. Tu piblicacion no debe superar los 250 caracteres",
            },
            {
                "role": "user",
                "content": " Genera una publicacion sobre el proces de limpieza de datos con pandas",
            },
        ],
        max_tokens=200,
    )

    return response.choices[0].message.content.strip()


print(generar_texto_post())
