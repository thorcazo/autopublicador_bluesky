from atproto import Client, client_utils
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("bs-username")
password = os.getenv("bs-password")


def post_image_with_text(img_path, text_post="", img_alt="", tags: list = []):
    if len(text_post) > 300:
        raise ValueError(
            f"El texto excede el límite de 300 caracteres. Longitud actual: {len(text_post)}"
        )

    client = Client()
    client.login(username, password)

    with open(img_path, "rb") as f:
        img_data = f.read()

    # Construcción del texto enriquecido con etiquetas
    tb = client_utils.TextBuilder()
    tb.text(text_post)

    for tag in tags:
        if tag:
            tb.text(" ")
            tb.tag(tag, f"did:plc:{tag}")

    # Publicar la imagen con el aspecto definido
    client.send_image(text=tb, image=img_data, image_alt=img_alt)


def send_post(text_post):
    if len(text_post) > 300:
        raise ValueError(
            f"El texto excede el límite de 300 caracteres. Longitud actual: {len(text_post)}"
        )

    client = Client()
    client.login(username, password)
    # Construcción del texto enriquecido
    tb = client_utils.TextBuilder()
    tb.text(text_post)

    # Enviar el post de texto enriquecido
    post_ref = client.send_post(tb)
    print("Post reference:", post_ref)
