from atproto import Client, client_utils
from dotenv import load_dotenv
import os
import requests


DID_URL = "https://bsky.social/xrpc/com.atproto.identity.resolveHandle"  # resolver el identificador descaentralizado de un usuario a partir de su handle en Bluesky.
API_KEY_URL = "https://bsky.social/xrpc/com.atproto.server.createSession"  # Crea una sesion de autenticacion en la API de Bluesky. Autentica al usuario y genera un token de acceso.
FEED_URL = "https://bsky.social/xrpc/app.bsky.feed.getAuthorFeed"  # Obtiene las publicaciones de un usuario.
POST_FEED_URL = "https://bsky.social/xrpc/com.atproto.repo.createRecord"  # Utilizada para crear una nueva publicacion.


load_dotenv()

username = os.getenv("bs-username")
password = os.getenv("bs-password")


def resolve_did(handle):
    handle_url = f"{DID_URL}?handle={handle}"
    response = requests.get(handle_url)
    response.raise_for_status()
    did = response.json().get("did")
    return did


# print(resolve_did(username))


# Obtener token de autenticacion: Utiliza el DID y la contraseña de aplicacion para obtener el tiken de autenticacion


def get_auth_token(did, app_password):
    payload = {"identifier": did, "password": app_password}
    response = requests.post(API_KEY_URL, json=payload)
    response.raise_for_status()
    token = response.json().get("accessJwt")
    return token


# print(get_auth_token(resolve_did(username), password))


# Recuperar las publicaciones de un usuario: Con el token de autenticacion, obten el feed de publicaciones de un usuario


def get_user_posts(handle, token, limit=2):
    feed_url = f"{FEED_URL}?actor={handle}&limit={limit}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(feed_url, headers=headers)
    response.raise_for_status()
    feed = response.json().get("feed", [])

    for item in feed:
        post = item.get("post", {}).get("record", {})
        print(f"Date: {post.get('createdAt')}")
        print(f"Text: {post.get('text')}")


get_user_posts(username, get_auth_token(resolve_did(username), password))
