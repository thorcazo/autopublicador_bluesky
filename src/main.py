#!/usr/bin/env python

from services.post_service import send_post, post_image_with_text
from pathlib import Path
from api.api_client_openai import generate_text_post

# TODO: importar cronjob para automatizar la publicación de posts

# Ruta relativa a la imagen
image_path = Path(__file__).parent / "img_posts/pandas_post.png"


# Genera un texto con OpenAI
generate_text = generate_text_post(limit_characters=400)

# Publica el texto generado
send_post(generate_text)

# post_image_with_text(
#     img_path=image_path,
#     text_post="""Estoy aprendiendo pandas para análisis y limpieza de datos.
# Uso .dropna() para eliminar nulos y .fillna() para rellenarlos. Tip: para datos numéricos, uso la media para evitar sesgos: df['columna'].fillna(df['columna'].mean(), inplace=True).
# """,
#     img_alt="imagen con código pandas",
#     tags=["pandas", "bigdata"],  # Etiquetas como lista
# )
