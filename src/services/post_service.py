from atproto import Client, client_utils
from dotenv import load_dotenv
from datetime import datetime
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
    # Dividir el texto en fragmentos si supera los 300 caracteres
    def divide_text(text, max_length=300):
        words = text.split()
        chunks = []
        current_chunk = ""

        for word in words:
            if len(current_chunk) + len(word) + 1 > max_length:
                chunks.append(current_chunk.strip())
                current_chunk = word
            else:
                current_chunk += " " + word
        if current_chunk:
            chunks.append(current_chunk.strip())
        return chunks

    client = Client()
    client.login(username, password)

    # Si el texto no supera los 300 caracteres, publica directamente
    if len(text_post) <= 300:
        post_ref = client.send_post(text_post)
        print("Post reference:", post_ref)
        return post_ref

    # Si supera los 300 caracteres, divide el texto en fragmentos
    chunks = divide_text(text_post)
    previous_post_ref = None  # Para almacenar la referencia del post anterior

    for i, chunk in enumerate(chunks):
        # Crear el objeto record con texto y marca de tiempo
        record = {
            "$type": "app.bsky.feed.post",
            "text": chunk,  # Aquí usamos directamente el fragmento del texto
            "createdAt": datetime.utcnow().isoformat() + "Z",  # Formato ISO 8601
        }

        # Si hay un post anterior, configura las referencias de respuesta
        if previous_post_ref:
            record["reply"] = {
                "root": {
                    "uri": previous_post_ref["uri"],
                    "cid": previous_post_ref["cid"],
                },
                "parent": {
                    "uri": previous_post_ref["uri"],
                    "cid": previous_post_ref["cid"],
                },
            }

        # Enviar el post o respuesta
        post_ref = client.app.bsky.feed.post.create(
            repo=client._session.did, record=record
        )
        print(f"Chunk {i + 1}/{len(chunks)} reference:", post_ref)

        # Actualizar la referencia para el próximo post en el hilo
        previous_post_ref = post_ref

    return previous_post_ref
