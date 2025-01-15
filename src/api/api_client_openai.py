from openai import OpenAI
from dotenv import load_dotenv
import os
import random

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Publicar en BlueSky (mejorado)
def generate_text_post(topic=None, limit_characters=250):
    # Temas disponibles
    topics = [
        "Ingeniería de datos",
        "Pandas: métodos y análisis exploratorio",
        "Numpy en ingeniería de datos",
        "Limpieza de datos",
        "Visualización con Matplotlib",
        "Visualización con Seaborn",
    ]

    # Seleccionar tema aleatorio si no se proporciona uno
    if topic is None:
        topic = random.choice(topics)

    # Generar prompts dinámicos basados en el tema
    user_prompts = {
        "Ingeniería de datos": [
            "Habla sobre el papel de la ingeniería de datos en proyectos modernos.",
            "Escribe sobre un día típico como ingeniero de datos.",
        ],
        "Pandas: métodos y análisis exploratorio": [
            "Cómo cargar y explorar un DataFrame con pandas.",
            "Describe el uso de pandas para el análisis exploratorio de datos.",
        ],
        "Numpy en ingeniería de datos": [
            "Habla sobre cómo numpy optimiza el manejo de datos en ingeniería.",
            "Describe un ejemplo de uso de numpy junto con pandas.",
        ],
        "Limpieza de datos": [
            "Cómo identificar y manejar datos nulos con pandas.",
            "Comparte consejos sobre limpieza de datos en proyectos reales.",
        ],
        "Visualización con Matplotlib": [
            "Describe cómo usar Matplotlib para gráficos simples.",
            "Explica un ejemplo de visualización combinando pandas y Matplotlib.",
        ],
        "Visualización con Seaborn": [
            "Habla sobre cómo Seaborn mejora las visualizaciones estadísticas.",
            "Explica el uso de Seaborn para crear gráficos avanzados.",
        ],
    }

    user_content = random.choice(
        user_prompts.get(topic, ["Habla sobre ingeniería de datos."])
    )

    # Generar contenido con OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {
                "role": "system",
                "content": f"Eres un generador de posts cortos sobre ingeniería de datos y programación web. El contenido debe ser claro, dinámico. Es extrictamente necesario no puede superar los {limit_characters} caracteres. Debes comportarte como si fuera tu el dieño del perfil de la red social. Por lo que tu respuesta el texto generado para el público objetivo de la red social",
            },
            {
                "role": "user",
                "content": user_content,
            },
        ],
        max_tokens=200,
    )

    return response.choices[0].message.content.strip()


print(generate_text_post())
