from openai import OpenAI
from dotenv import load_dotenv
import os
import random

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Publicar en BlueSky (actualizado)
def generate_text_post(topic=None, limit_characters=250):
    # Temas disponibles
    topics = [
        "Tendencias en diseño web 2025",
        "React/Angular/Vue",
        "CSS moderno",
        "Performance en el frontend",
        "JavaScript avanzado",
        "Buenas prácticas en APIs RESTful",
        "Microservicios vs Monolitos",
        "Bases de datos",
        "Node.js",
        "Seguridad en el backend",
        "El mundo de DevOps",
        "Trabajo remoto para programadores",
        "Proyectos personales para mejorar tu portafolio",
        "El impacto de la IA en la programación",
        "Cómo aprender a programar más rápido",
        "Consejos para entrevistas técnicas",
    ]

    # Seleccionar tema aleatorio si no se proporciona uno
    if topic is None:
        topic = random.choice(topics)

    # Generar prompts dinámicos basados en el tema
    prompts = {
        "Tendencias en diseño web 2025": [
            "Habla sobre el uso de colores gradientes modernos en diseño web.",
            "Explica la importancia de las microinteracciones en la experiencia del usuario.",
            "Describe cómo implementar un diseño accesible en proyectos web.",
        ],
        "React/Angular/Vue": [
            "Comparación entre frameworks: ¿Cuál elegir para tu próximo proyecto?",
            "Consejos para usar hooks avanzados en React.",
            "Patrones de diseño escalables con Vue.",
        ],
        "CSS moderno": [
            "Cómo usar CSS Grid y Flexbox de manera eficiente.",
            "Optimización de temas dinámicos con variables CSS.",
            "Crea animaciones avanzadas usando @keyframes.",
        ],
        "Performance en el frontend": [
            "Técnicas para reducir el tiempo de carga en proyectos web.",
            "Cómo medir el rendimiento con Lighthouse.",
        ],
        "JavaScript avanzado": [
            "Diferencias entre var, let y const explicadas con ejemplos.",
            "Mejores prácticas para usar Async/Await.",
            "Ejemplos prácticos de funciones de alto orden.",
        ],
        "Buenas prácticas en APIs RESTful": [
            "Cómo diseñar endpoints claros y eficientes.",
            "Implementación de validaciones con Joi o Yup.",
            "Consejos para agregar paginación y filtros avanzados.",
        ],
        "Microservicios vs Monolitos": [
            "Ventajas y desventajas de arquitecturas monolíticas.",
            "Herramientas populares para trabajar con microservicios.",
        ],
        "Bases de datos": [
            "Diferencias entre bases de datos relacionales y NoSQL.",
            "Introducción a bases de datos distribuidas.",
            "Cómo optimizar consultas SQL.",
        ],
        "Node.js": [
            "Manejo eficiente de solicitudes con Node.js.",
            "Creación de servidores rápidos usando Express o Fastify.",
            "Uso de Streams en Node.js para datos en tiempo real.",
        ],
        "Seguridad en el backend": [
            "Implementación de OAuth 2.0 y JWT en tus proyectos.",
            "Cómo evitar vulnerabilidades comunes como SQL Injection.",
            "Usa helmet.js para proteger tu API.",
        ],
        "El mundo de DevOps": [
            "¿Qué es DevOps y por qué deberías aprenderlo?",
            "Cómo configurar pipelines CI/CD con Jenkins o GitHub Actions.",
        ],
        "Trabajo remoto para programadores": [
            "Herramientas para trabajar en equipo a distancia.",
            "Consejos para mantener la productividad desde casa.",
        ],
        "Proyectos personales para mejorar tu portafolio": [
            "Ideas de proyectos para principiantes e intermedios.",
            "Cómo documentar un proyecto para destacar en GitHub.",
        ],
        "El impacto de la IA en la programación": [
            "Cómo usar herramientas como ChatGPT para ser más productivo.",
            "Aspectos éticos de la programación asistida por IA.",
        ],
        "Cómo aprender a programar más rápido": [
            "Métodos efectivos para aprender un nuevo lenguaje.",
            "Recursos gratuitos y de pago recomendados para aprender programación.",
        ],
        "Consejos para entrevistas técnicas": [
            "Ejercicios comunes de algoritmos y estructuras de datos.",
            "Cómo prepararte para preguntas sobre diseño de sistemas.",
        ],
    }

    # Seleccionar un prompt basado en el tema
    prompt_content = random.choice(prompts.get(topic, ["Habla sobre programación y desarrollo."]))

    # Generar contenido con OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {
                "role": "system",
                "content": f"Eres un generador de posts cortos sobre programación, diseño web y mejores prácticas en desarrollo. El contenido debe ser claro, interesante y útil. Utiliza un tono personal, habla en primera persona. No generes fragmentos de código de ejemplo, solo nombra los atributos o metodos específicos de los que estés hablando. Mantener la publicacíón dentro de un límite de {limit_characters} caracteres. Tema: {prompt_content}",
            }
        ],
        max_tokens=300,
    )

    return response.choices[0].message.content.strip()

# Ejemplo de uso
print(generate_text_post())
